# inquiry-box — 1권 12장 예제 MCP 서버

12장 따라하기에서 Claude Code로 만드는 문의함 서버의 예제입니다. 막히면 내 `server.py`와 비교해 보세요.
`inbox/2026-11/`에는 샘플 문의 5통이 들어 있습니다.

```bash
uv sync                      # 의존성 설치
uv run pytest -q             # 테스트 실행
claude mcp add inquiry-box -- uv run --directory "$(pwd)" server.py   # 이 폴더에서 실행해 Claude Code에 등록
```
