"""문의함(inquiry-box) MCP 서버 — 고객 문의를 읽고 답장 초안을 저장한다."""

import logging
import os
import re
from pathlib import Path
from typing import Annotated

from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.exceptions import ToolError
from mcp.types import ToolAnnotations
from pydantic import Field

# stdout은 Claude와 대화하는 통로라서 print를 쓰면 안 된다. 로그는 stderr로 보낸다.
logging.basicConfig(level=logging.INFO)  # basicConfig의 기본 출력이 stderr다
log = logging.getLogger("inquiry-box")

# 데이터 폴더는 환경변수로 바꿀 수 있게 하고, 없으면 이 파일 옆 폴더를 쓴다.
BOX_DIR = Path(os.environ.get("INQUIRY_BOX_DIR", Path(__file__).parent))
INBOX = BOX_DIR / "inbox"
DRAFTS = BOX_DIR / "drafts"

# 형식을 정규식으로 못 박아 두면 "../" 같은 경로 탈출이 들어올 틈이 없다.
MONTH_RE = re.compile(r"\d{4}-(0[1-9]|1[0-2])")
ID_RE = re.compile(r"(\d{4}-(?:0[1-9]|1[0-2]))-\d{3}")

mcp = MCPServer("inquiry-box")


def find_inquiry(inquiry_id: str) -> Path:
    match = ID_RE.fullmatch(inquiry_id)  # fullmatch: 문자열 전체가 형식과 같아야 통과
    if not match:
        # ToolError로 던져야 이 한국어 메시지가 Claude에게 그대로 전달된다.
        raise ToolError(f"문의 번호 형식이 잘못되었습니다: {inquiry_id!r}. 예: 2026-11-001")
    path = INBOX / match.group(1) / f"{inquiry_id}.txt"
    if not path.exists():
        raise ToolError(f"문의 {inquiry_id}를 찾을 수 없습니다. list_inquiries로 번호를 확인하세요.")
    return path


@mcp.tool(
    description="지정한 달에 받은 고객 문의 목록(번호, 제목, 받은 날)을 돌려줍니다. "
    "어떤 문의가 있는지 훑어볼 때 씁니다. 본문은 돌려주지 않으니 read_inquiry를 쓰세요.",
    annotations=ToolAnnotations(
        title="문의 목록 보기",
        read_only_hint=True,  # 아무것도 바꾸지 않는다
        destructive_hint=False,
        idempotent_hint=True,  # 몇 번 불러도 결과가 같다
        open_world_hint=False,  # 이 컴퓨터의 폴더만 본다
    ),
)
def list_inquiries(
    month: Annotated[str, Field(description="조회할 달. YYYY-MM 형식 (예: 2026-11)")],
) -> list[dict[str, str]]:
    if not MONTH_RE.fullmatch(month):
        raise ToolError(f"월 형식이 잘못되었습니다: {month!r}. 예: 2026-11")
    result = []
    for path in sorted((INBOX / month).glob("*.txt")):  # 폴더가 없으면 빈 목록이 된다
        lines = path.read_text(encoding="utf-8").splitlines()
        subject = lines[0].removeprefix("제목:").strip()  # 첫 줄: "제목: ..."
        received = lines[1].removeprefix("받은 날:").strip()  # 둘째 줄: "받은 날: ..."
        result.append({"id": path.stem, "subject": subject, "received": received})
    return result


@mcp.tool(
    description="문의 하나의 전문(제목, 받은 날, 본문)을 돌려줍니다. "
    "답장을 쓰기 전에 내용을 확인할 때 씁니다. 문의 내용을 바꾸지 않습니다.",
    annotations=ToolAnnotations(
        title="문의 읽기",
        read_only_hint=True,
        destructive_hint=False,
        idempotent_hint=True,
        open_world_hint=False,
    ),
)
def read_inquiry(
    inquiry_id: Annotated[str, Field(description="문의 번호. YYYY-MM-NNN 형식 (예: 2026-11-001)")],
) -> str:
    return find_inquiry(inquiry_id).read_text(encoding="utf-8")


@mcp.tool(
    description="답장 초안을 drafts 폴더에 저장합니다. 고객에게 보내지 않으며, 사람이 검토한 뒤 보냅니다. "
    "같은 문의의 초안이 이미 있으면 덮어쓰지 않고 오류를 돌려줍니다.",
    annotations=ToolAnnotations(
        title="답장 초안 저장",
        read_only_hint=False,  # 파일을 새로 만든다
        destructive_hint=False,  # 기존 파일을 지우거나 덮어쓰지 않는다
        idempotent_hint=False,  # 두 번째 호출은 오류가 나므로 결과가 다르다
        open_world_hint=False,
    ),
)
def save_reply_draft(
    inquiry_id: Annotated[str, Field(description="답장할 문의 번호. YYYY-MM-NNN 형식")],
    text: Annotated[str, Field(description="답장 초안 본문 (마크다운)")],
) -> str:
    find_inquiry(inquiry_id)  # 없는 문의에 초안을 만들지 않도록 먼저 확인한다
    DRAFTS.mkdir(parents=True, exist_ok=True)
    path = DRAFTS / f"{inquiry_id}.md"
    try:
        # "x" 모드는 파일이 이미 있으면 실패한다. 확인과 생성을 한 번에 해서 덮어쓰기를 막는다.
        with path.open("x", encoding="utf-8") as f:
            f.write(text)
    except FileExistsError as err:
        raise ToolError(f"{inquiry_id}의 초안이 이미 있습니다. 기존 초안은 그대로 두었습니다.") from err
    log.info("초안 저장: %s", path)
    return f"초안을 저장했습니다: drafts/{inquiry_id}.md (고객에게 보내지 않았습니다)"


if __name__ == "__main__":
    mcp.run()  # 기본값이 stdio다
