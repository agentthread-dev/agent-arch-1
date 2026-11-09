# inquiry-box — 12장 혼자하기 예시 (list_drafts를 더한 서버)

12장 예제 서버에 혼자하기의 `list_drafts` 도구를 하나 더한 모습입니다. 원고에는 안내판만 실려 있어,
이 서버와 테스트는 예제 꾸러미에만 있는 **예시 답안 하나**입니다. 내 서버가 다르게 생겼어도 안내판의
약속(입력 없음, 초안 내용은 돌려주지 않음, 읽기 전용)을 지키고 테스트가 통과하면 됩니다.

바뀐 곳:

- `server.py` — 맨 아래에 `list_drafts` 도구 (돌려주는 것: 문의 번호, 파일 크기(바이트), 저장 시각)
- `tests/test_list_drafts.py` — 초안이 없으면 빈 목록, 한 번 저장한 뒤엔 한 건, 다른 파일은 건너뜀, 아무것도 바꾸지 않음
- `tests/test_protocol.py` — 도구가 네 개로 늘었는지, `list_drafts`가 읽기 전용으로 표시됐는지

```bash
uv sync                      # 의존성 설치
uv run pytest -q             # 테스트 실행
claude mcp add inquiry-box -- uv run --directory "$(pwd)" server.py   # 이미 등록했다면 Claude Code만 새로 열기
```

Claude Code를 새로 열고 `/mcp`에서 inquiry-box의 도구가 네 개인지 확인하세요.
