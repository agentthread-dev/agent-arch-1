import asyncio
import os
import sys

from conftest import PROJECT
from mcp import Client, StdioServerParameters


async def talk_to_server():
    # Claude Code가 하듯이 server.py를 별도 프로세스로 띄우고 stdin/stdout으로 대화한다.
    params = StdioServerParameters(
        command=sys.executable,
        args=[str(PROJECT / "server.py")],
        env={"INQUIRY_BOX_DIR": os.environ["INQUIRY_BOX_DIR"]},
    )
    # mode="legacy"는 initialize 핸드셰이크로 연결을 시작하게 한다.
    async with Client(params, mode="legacy") as client:
        tools = await client.list_tools()
        result = await client.call_tool("list_inquiries", {"month": "2026-11"})
        bad = await client.call_tool("read_inquiry", {"inquiry_id": "../server"})
        before = await client.call_tool("list_drafts", {})
        await client.call_tool("save_reply_draft", {"inquiry_id": "2026-11-001", "text": "초안"})
        after = await client.call_tool("list_drafts", {})
        return client.server_info, tools.tools, result, bad, (before, after)


def test_stdio_round_trip(box_dir):
    info, tools, result, bad, (before, after) = asyncio.run(talk_to_server())

    assert info.name == "inquiry-box"  # initialize가 성공했다
    by_name = {t.name: t for t in tools}
    assert sorted(by_name) == ["list_drafts", "list_inquiries", "read_inquiry", "save_reply_draft"]  # 네 개로 늘었다
    assert by_name["list_inquiries"].annotations.read_only_hint is True
    drafts = by_name["list_drafts"].annotations
    assert (drafts.read_only_hint, drafts.destructive_hint, drafts.idempotent_hint) == (True, False, True)
    assert by_name["list_drafts"].input_schema.get("properties", {}) == {}  # 입력 없음
    assert by_name["read_inquiry"].annotations.read_only_hint is True
    save = by_name["save_reply_draft"].annotations
    assert (save.read_only_hint, save.destructive_hint) == (False, False)
    assert "description" in by_name["read_inquiry"].input_schema["properties"]["inquiry_id"]

    assert not result.is_error
    assert len(result.structured_content["result"]) == 5

    assert bad.is_error
    assert "형식이 잘못" in bad.content[0].text  # 한국어 오류가 그대로 전달된다

    assert before.structured_content["result"] == []  # 초안이 없으면 빈 목록
    (item,) = after.structured_content["result"]  # save_reply_draft 한 번 뒤에는 한 건
    assert item["id"] == "2026-11-001"
