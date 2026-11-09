"""12장 혼자하기 — list_drafts 안내판의 '테스트' 줄과 읽기 전용 약속을 확인한다."""

import importlib
import os
from datetime import datetime

import pytest


@pytest.fixture
def server(box_dir):
    import server

    return importlib.reload(server)


def test_empty_when_no_drafts(server, box_dir):
    assert server.list_drafts() == []
    assert not (box_dir / "drafts").exists()  # 읽기 전용: 목록을 보느라 폴더를 만들지 않는다


def test_one_item_after_one_save(server):
    server.save_reply_draft("2026-11-001", "안녕하세요. 확인 후 안내드리겠습니다.")
    (item,) = server.list_drafts()
    assert set(item) == {"id", "size_bytes", "saved_at"}  # 초안 내용은 돌려주지 않는다
    assert item["id"] == "2026-11-001"
    assert item["size_bytes"] == len("안녕하세요. 확인 후 안내드리겠습니다.".encode())
    saved = datetime.fromisoformat(item["saved_at"])
    assert saved.tzinfo is not None  # 시간대가 붙은 시각


def test_sorted_by_inquiry_id(server):
    server.save_reply_draft("2026-11-003", "셋")
    server.save_reply_draft("2026-11-001", "하나")
    assert [d["id"] for d in server.list_drafts()] == ["2026-11-001", "2026-11-003"]


def test_skips_files_not_made_by_save(server, box_dir):
    server.save_reply_draft("2026-11-002", "둘")
    drafts = box_dir / "drafts"
    (drafts / "메모.md").write_text("사람이 넣은 메모", encoding="utf-8")
    (drafts / "2026-11-004.txt").write_text("확장자가 다름", encoding="utf-8")
    (drafts / "2026-11-005.md").mkdir()  # 이름은 맞지만 폴더
    outside = box_dir / "secret.md"
    outside.write_text("폴더 밖 파일", encoding="utf-8")
    os.symlink(outside, drafts / "2026-11-001.md")  # 이름은 맞지만 폴더 밖을 가리키는 바로가기
    assert [d["id"] for d in server.list_drafts()] == ["2026-11-002"]


def test_does_not_change_drafts(server, box_dir):
    server.save_reply_draft("2026-11-001", "초안")
    path = box_dir / "drafts" / "2026-11-001.md"
    before = path.stat().st_mtime_ns
    assert server.list_drafts() == server.list_drafts()  # 몇 번 불러도 같다
    assert path.stat().st_mtime_ns == before
    assert path.read_text(encoding="utf-8") == "초안"
