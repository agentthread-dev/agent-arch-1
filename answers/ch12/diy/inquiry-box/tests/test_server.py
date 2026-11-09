import importlib

import pytest
from mcp.server.mcpserver.exceptions import ToolError


@pytest.fixture
def server(box_dir):
    # server.py는 import할 때 INQUIRY_BOX_DIR을 읽으므로, 환경변수를 바꾼 뒤 다시 불러온다.
    import server

    return importlib.reload(server)


def test_list_inquiries_returns_five_without_body(server):
    items = server.list_inquiries("2026-11")
    assert [i["id"] for i in items] == [f"2026-11-00{n}" for n in range(1, 6)]
    assert items[0] == {
        "id": "2026-11-001",
        "subject": "주문한 지 4일인데 아직 출발 안 했어요",
        "received": "2026-11-03",
    }


def test_list_inquiries_empty_month(server):
    assert server.list_inquiries("2026-10") == []


def test_read_inquiry_returns_full_text(server):
    text = server.read_inquiry("2026-11-003")
    assert text.startswith("제목: 반품했는데 환불은 언제 되나요")
    assert "카드 결제" in text


@pytest.mark.parametrize("bad", ["2026-13", "../2026-11", "2026-11/..", "2026-11\n", ""])
def test_list_inquiries_rejects_bad_month(server, bad):
    with pytest.raises(ToolError, match="월 형식"):
        server.list_inquiries(bad)


@pytest.mark.parametrize("bad", ["../../server", "2026-11/../../x", "2026-11-1", "2026-11-001.txt"])
def test_read_inquiry_rejects_bad_id(server, bad):
    with pytest.raises(ToolError, match="형식이 잘못"):
        server.read_inquiry(bad)


def test_read_inquiry_missing_id(server):
    with pytest.raises(ToolError, match="찾을 수 없습니다"):
        server.read_inquiry("2026-11-999")


def test_save_reply_draft_refuses_overwrite(server, box_dir):
    server.save_reply_draft("2026-11-001", "첫 번째 초안")
    with pytest.raises(ToolError, match="이미 있습니다"):
        server.save_reply_draft("2026-11-001", "두 번째 초안")
    assert (box_dir / "drafts" / "2026-11-001.md").read_text(encoding="utf-8") == "첫 번째 초안"


def test_save_reply_draft_rejects_missing_inquiry(server, box_dir):
    with pytest.raises(ToolError, match="찾을 수 없습니다"):
        server.save_reply_draft("2026-11-999", "초안")
    assert not (box_dir / "drafts" / "2026-11-999.md").exists()
