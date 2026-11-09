import shutil
from pathlib import Path

import pytest

PROJECT = Path(__file__).parent.parent


@pytest.fixture
def box_dir(tmp_path, monkeypatch):
    """샘플 문의를 임시 폴더에 복사해, 원본 데이터를 건드리지 않고 시험한다."""
    shutil.copytree(PROJECT / "inbox", tmp_path / "inbox")
    monkeypatch.setenv("INQUIRY_BOX_DIR", str(tmp_path))
    return tmp_path
