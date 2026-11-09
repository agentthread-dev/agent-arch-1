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
        return client.server_info, tools.tools, result, bad


def test_stdio_round_trip(box_dir):
    info, tools, result, bad = asyncio.run(talk_to_server())

    assert info.name == "inquiry-box"  # initialize가 성공했다
    by_name = {t.name: t for t in tools}
    assert sorted(by_name) == ["list_inquiries", "read_inquiry", "save_reply_draft"]
    assert by_name["list_inquiries"].annotations.read_only_hint is True
    assert by_name["read_inquiry"].annotations.read_only_hint is True
    save = by_name["save_reply_draft"].annotations
    assert (save.read_only_hint, save.destructive_hint) == (False, False)
    assert "description" in by_name["read_inquiry"].input_schema["properties"]["inquiry_id"]

    assert not result.is_error
    assert len(result.structured_content["result"]) == 5

    assert bad.is_error
    assert "형식이 잘못" in bad.content[0].text  # 한국어 오류가 그대로 전달된다
