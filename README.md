# 에이전트 아키텍처 마스터 1권 — Skill과 MCP로 일하는 AI 만들기

책 「에이전트 아키텍처 마스터 1권 — Skill과 MCP로 일하는 AI 만들기」의 예제 파일과 실습 결과물, 예시 답안입니다.

## 받는 법

터미널에서 홈 폴더로 받습니다. 책의 실습 작업 폴더(`~/book-code`)와 겹치지 않게 따로 둡니다.

```bash
cd ~
git clone https://github.com/agentthread-dev/agent-arch-1.git
```

git이 없다면 이 페이지의 **Code → Download ZIP**으로 받아 압축을 풀어도 됩니다. 책이 고쳐지면(정오표) 받은 폴더에서
`git pull`로 새 내용을 받을 수 있습니다. 책의 판·쇄에 맞춘 내용은 태그(`ed1` 등)로 남깁니다.

## 쓰는 법

- 장을 시작할 때 `start/chNN/`의 파일을 책이 말하는 작업 폴더로 **복사**해서 씁니다. 이 저장소 안에서 바로 실습하지 마세요.
- 장을 마친 뒤 내 파일을 `answers/chNN/`과 비교합니다. 달라도 틀린 것은 아닙니다. 책의 확인 기준으로 점검하세요.

## 저작권

© 2026 정원도. All rights reserved.

이 저장소의 파일은 책 독자의 학습을 위한 자료입니다. 책과 함께 공부하거나 내 업무에 맞게 고쳐 연습하는 데는
자유롭게 쓰셔도 됩니다. 다만 파일을 그대로 다시 배포하거나 판매·강의 자료 등 상업적으로 쓰려면 먼저 저자에게 허락을 받아 주세요.

---

## 장별 안내

- `start/chNN/` — 그 장을 **시작할 때** 필요한 재료입니다. 장의 작업 폴더로 복사해서 씁니다.
- `answers/chNN/` — 그 장을 **마쳤을 때** 생기는 파일과 혼자하기(`diy/`)·도전하기(`challenge/`) 예시 답안입니다.
  장마다 **그 장에서 새로 만들거나 고친 파일만** 담았습니다. 앞 장에서 만든 파일은 앞 장의 `answers/`에 있습니다.
- 폴더 경로는 작업 폴더 기준입니다. 예를 들어 `answers/chNN/inquiry-box/.claude/settings.json`은
  작업 폴더 `inquiry-box/` 안의 `.claude/settings.json`입니다. `.claude/`처럼 점으로 시작하는 폴더는 숨은 폴더라
  Finder에서 안 보일 수 있습니다(`ls -a`로 확인).
- `prompts/`는 책에 실린 긴 요청문, `forms/`는 빈 양식입니다. 복사해서 붙여넣으세요.
- Claude가 만드는 결과물(답장 초안, 보고서 등)은 실행마다 달라서 싣지 않았습니다. 장별 메모를 보세요.

| 장 | start에 있는 것 | answers에 있는 것 | 원고 위치 |
|---|---|---|---|
| 1장 AI 에이전트 시대의 변화 읽기 | `meeting_memo.txt`<br>`prompts/delegated-request.txt` — 위임형 요청문<br>`forms/observation-log.md` — 관찰 일지 (P1-①)<br>`forms/agent-candidates.md` — 에이전트 후보 진단표 (P1-③) | `diy/weekly-report-request.txt` — 혼자하기 예시 (P1-②) | 1장 '로 저장하세요.' 다음 코드<br>1장 '### 4단계:' 다음 코드<br>1장 [표 1-2]<br>1장 [표 1-3]<br>1장 '예시 답안 — '주간 업무 보고서' 위임형 요청문' 다음 코드 |
| 2장 Skill이란 무엇인가 | `forms/observation-log-extended.md` — 확장된 관찰 일지<br>`forms/description-hit-test.md` — 적중률 실험표 (P1-⑤) | `meeting-followup/SKILL.md`<br>`diy/weekly-report/SKILL.md` — 혼자하기 예시 (P1-④) | 2장 [표 2-2]<br>2장 [표 2-3]<br>2장 '### 2단계: SKILL.md 작성하기' 다음 코드<br>2장 '폴더 이름: weekly-report' 다음 코드 |
| 3장 MCP란 무엇인가 | `book-practice/meeting_memo.txt`<br>`book-practice/weekly-notes/this_week.txt` — 혼자하기 예시가 읽는 업무 메모 (4장 혼자하기도 씀) (꾸러미 전용 예시) | `diy/requests.txt` — 혼자하기 예시 요청문 (P1-⑦)<br>`challenge/connection-card.txt` — 연결 명세 카드 예 (P1-⑧) | 1장 1단계 (1장 start와 같음)<br>원고 밖 — 3장 혼자하기 예시 답안의 폴더 구성에 이름만 나옴<br>3장 '요청문:' 다음 코드<br>3장 [코드 3-1] |
| 4장 두 기술의 연결고리 | `prompts/requests.txt` — 초안·확인·마무리 요청문<br>`forms/skill-map.md` — 기술 지도 (P1-⑨) | `mailbox-rules.txt`<br>`diy/weekly-notes-mailbox.txt` — 우편함 규칙과 요청문 세 개 (P1-⑩)<br>`challenge/roadmap.txt` — 도입 로드맵 예 (P1-⑪) | 4장 '### 2단계: 초안' 다음 코드, 4장 '### 3단계: 확인' 다음 코드, 4장 '### 4단계: 마무리' 다음 코드<br>4장 [표 4-3]<br>4장 '### 1단계: 우편함 정하기' 다음 코드<br>4장 '예시 답안 — '주간 업무 보고서' 우편함 규칙' 다음 코드, 4장 '예시 답안 — '주간 업무 보고서' 우편함 규칙' 다음 코드, 4장 '예시 답안 — '주간 업무 보고서' 우편함 규칙' 다음 코드, 4장 '예시 답안 — '주간 업무 보고서' 우편함 규칙' 다음 코드<br>4장 [코드 4-1] |
| 5장 첫 Skill 만들기 | `book-practice/ch07/inquiry_01.txt`<br>`book-practice/ch07/inquiry_02.txt`<br>`book-practice/ch07/inquiry_03.txt`<br>`forms/test-table.md` — 테스트 표 (P2-①) | `design-memo.txt` — Skill 설계 메모<br>`book-skills/customer-reply/references/policy.md`<br>`book-skills/customer-reply/SKILL.md`<br>`challenge/description-pieces.txt` — description 세 조각<br>`diy/weekly-report/SKILL.md` — 다듬은 weekly-report SKILL.md 전체 (P2-②)<br>`diy/weekly-report/references/report-format.md` — 혼자하기 예시 양식 (P2-②) (꾸러미 전용 예시) | 5장 'inquiry_01.txt — 정책으로 바로 답할 수 있는 문의' 다음 코드<br>5장 'inquiry_02.txt — 정책 일부만으로 답할 수 있는 문의' 다음 코드<br>5장 'inquiry_03.txt — 정책 밖을 요구하는 문의' 다음 코드<br>5장 [표 5-3]<br>5장 '### 1단계: 설계 메모부터 쓰기' 다음 코드<br>5장 '### 3단계: 참고 파일(policy.md) 쓰기' 다음 코드<br>5장 [코드 5-3]<br>5장 '### 과제: description을 한 조각씩 빼 보며' 다음 코드<br>2장 혼자하기 예시 + 5장 예시 답안의 '본문에 추가한 줄'·'description 끝에 추가한 문장'<br>원고 밖 — 5장 혼자하기 예시 답안의 폴더 구성에 칸 이름만 나옴 |
| 6장 Skill 설계 원칙 | `cs-helper/SKILL.md` — 진단용 (설치하지 않음)<br>`forms/skill-design-checklist.txt` — 설계 점검표 양식<br>`book-practice/ch08/inquiries_batch.txt` | `book-skills/inquiry-classify/references/categories.md`<br>`book-skills/inquiry-classify/SKILL.md`<br>`diy/weekly-report-checklist.txt` — 혼자하기 예시 (P2-⑥) | 6장 '설치하지 말고 읽기만 하세요.' 다음 코드<br>6장 '아래 점검표를 메모장에 옮기고' 다음 코드<br>6장 '먼저 분류용 자료를 하나 더 만드세요.' 다음 코드<br>6장 [코드 6-2]<br>6장 [코드 6-3]<br>6장 '예시 답안 — weekly-report 점검과 수정' 다음 코드, 6장 '예시 답안 — weekly-report 점검과 수정' 다음 코드 |
| 7장 실전 Skill 제작 | `book-practice/ch09/month_summary.txt`<br>`forms/result-checklist.md` — 결과 점검표 (P2-⑦) | `book-skills/inquiry-monthly-report/assets/report-template.md`<br>`book-skills/inquiry-monthly-report/references/writing-rules.md`<br>`book-skills/inquiry-monthly-report/references/examples.md`<br>`book-skills/inquiry-monthly-report/SKILL.md`<br>`book-skills/inquiry-monthly-report-안내.txt` — 사용 안내와 변경 기록<br>`design-memo.txt` — Skill 설계 메모<br>`diy/meeting-agenda.txt` — 혼자하기 예시 (구조와 확인 기준 일부)<br>`challenge/inquiry-monthly-report/SKILL.md` — 절차 3번을 바꾼 SKILL.md (꾸러미 전용 예시)<br>`diy/book-skills/meeting-agenda/` — 혼자하기 예시 Skill (P2-⑧) (꾸러미 전용 예시)<br>`diy/book-skills/meeting-agenda-안내.txt` — 사용 안내와 변경 기록 (꾸러미 전용 예시)<br>`challenge/inquiry-monthly-report/scripts/` — 계산 스크립트 calc_changes.py (P2-⑨) (꾸러미 전용 예시)<br>`challenge/tests/` — 스크립트 테스트 (꾸러미 전용 예시) | 7장 '### 5단계: 분류 결과 형식으로 시험하기' 다음 코드<br>7장 [표 7-2]<br>7장 [코드 7-2]<br>7장 [코드 7-3]<br>7장 [코드 7-4]<br>7장 [코드 7-5]<br>7장 '① 사용 안내 한 장.' 다음 코드, 7장 '② 변경 기록.' 다음 코드<br>7장 '### 3단계: 설계 메모' 다음 코드<br>7장 '예시 답안 — '주간 팀 회의 안건지' Skill' 다음 코드, 7장 '예시 답안 — '주간 팀 회의 안건지' Skill' 다음 코드<br>7장 [코드 7-5] + 도전하기 '방향 제시'의 절차 3번 문장 (실행 방법 한 줄은 꾸러미에서 더함)<br>원고 밖 — 7장 혼자하기 예시 답안의 폴더 구조와 확인 기준 세 줄로 만듦<br>원고 밖 — 7장 혼자하기 예시 답안의 폴더 구조에 이름만 나옴<br>원고 밖 — 7장 도전하기의 폴더 구조에 이름과 역할만 나옴<br>원고 밖 — calc_changes.py 시험 (Skill 폴더 밖) |
| 8장 Skill 디버깅과 개선 | `book-skills/customer-reply/SKILL.md` — 동료가 바꾼 버그판<br>`book-skills/customer-reply/references/policy.md`<br>`colleague-changes.txt` — 동료가 바꾼 곳 (원고 그대로) | `debug-log.txt` — 디버깅 기록장 (P2-⑩)<br>`diy/monthly-report-debug-log.txt` — 혼자하기 예시 (P2-⑪)<br>`challenge/book-skills/건강검진.txt` — 건강검진 세트 (P2-⑫) (꾸러미 전용 예시) | 8장 1단계 '동료가 바꾼 곳' 세 군데를 5장 SKILL.md에 적용<br>5장 3단계 (바뀌지 않음)<br>8장 '아래 세 곳을 동료가 바꾼 대로 고칩니다.' 다음 코드<br>8장 '새로 보인 증상이 있다면 고친 줄에 덧붙이지 말고' 다음 코드<br>8장 '예시 답안 — inquiry-monthly-report의 '한눈에 보기' 개선' 다음 코드<br>원고 밖 — 8장 도전하기 '방향 제시'로 만듦 |
| 9장 [복합 실습] 여러 Skill 조합 자동화 | `book-practice/ch11/inquiries_nov.txt`<br>`book-practice/ch11/last_month.txt`<br>`prompts/one-request.txt` — ② 한 요청 요청문<br>`forms/flow-checklist.md` — 월말 흐름 점검표 | `book-skills/month-end-cs/SKILL.md`<br>`diy/week-end-report-order.md` — 혼자하기 예시 (순서 부분) | 9장 [코드 9-1]<br>9장 [코드 9-2]<br>9장 '### 2단계: ② 한 요청에 순서대로' 다음 코드<br>9장 [표 9-2]<br>9장 [코드 9-3]<br>9장 '예시 답안 — 주간 마감 흐름' 다음 코드 |
| 10장 MCP 서버 개념과 구조 | `forms/server-anatomy.txt` — 서버 해부도 양식 (P3-①) | `challenge/inquiry-box-signboard.txt` — 문의함 서버 안내판 (P3-③, 12장 재료) | 10장 [코드 10-3]<br>10장 '설명이 서로 겹쳐서 AI가 헷갈릴 만한 도구 쌍이 없는지' 다음 코드 |
| 11장 기존 MCP 서버 연결해 보기 | `book-reference/faq.txt`<br>`forms/preflight-checklist.txt` — 연결 전 점검표 | `claude_desktop_config.json` — reference-files를 적은 설정 파일<br>`three-ways-card.txt` — 세 길 비교 카드 양식 (P3-④)<br>`diy/claude_desktop_config.json` — customer-memory를 더한 설정 (P3-⑤)<br>`diy/preflight-customer-memory.txt` — customer-memory 점검표 예 | 11장 [코드 11-3]<br>11장 [코드 11-6]<br>11장 [코드 11-1]<br>11장 [코드 11-5]<br>11장 [코드 11-1] + [코드 11-7]<br>11장 '늘 때마다 줄이 하나 늘어납니다. 점검표는 이렇게 채웠습니다.' 다음 코드 |
| 12장 나만의 MCP 서버 만들기 (기초) | `prompts/make-server.txt` — 서버를 만들어 달라는 요청문 | `diy/list_drafts-signboard.txt` — 혼자하기 예시 (P3-⑧)<br>`inquiry-box/` — 예제 서버 (server.py, uv.lock), 테스트·샘플 문의 5통·pyproject<br>`diy/inquiry-box/` — 서버 바탕 (uv.lock), 테스트·샘플 문의 5통·pyproject, list_drafts를 더한 server.py와 테스트 (P3-⑧) (꾸러미 전용 예시) | 12장 [코드 12-3]<br>12장 '예시 답안 — list_drafts 안내판' 다음 코드<br>원고 밖 — 원고가 말하는 '예제 저장소' 서버 (코드 12-1·12-4와 같은 코드)<br>원고 밖 — 테스트 16개, 샘플 문의 5통 (2단계 요청의 [데이터])<br>원고 밖 — 12장 예제 서버를 바탕으로 혼자하기 list_drafts 안내판대로 만듦 |
| 13장 MCP 보안과 운영 고려사항 | `inquiry-box/inbox/2026-11/2026-11-006.txt` — 숨은 지시가 든 연습용 문의<br>`prompts/safe-request.txt` — 자료와 지시를 구분하게 하는 요청문 | `inquiry-box/.claude/settings.json`<br>`ops-checklist.txt` — 운영 점검표 (P3-⑩) | 13장 [코드 13-3]<br>13장 [코드 13-4]<br>13장 [코드 13-5]<br>13장 [코드 13-6] |
| 14장 [복합 실습] Skill + 자작 MCP 서버 워크플로우 | `prompts/fill-inbox.txt` — 문의함을 채우는 요청문<br>`book-practice/ch11/inquiries_nov.txt`<br>`book-practice/ch11/last_month.txt` | `inquiry-box/last_month.txt`<br>`inquiry-box/.claude/skills/month-end-mcp/SKILL.md`<br>`flow-card.txt` — 흐름 기록 카드 양식 (P3-⑬)<br>`diy/weekly-report-flow.txt` — 혼자하기 예시<br>`inquiry-box/inbox/` — 문의 12통 (저자 실행 결과) | 14장 [코드 14-2]<br>9장 1단계 (9장 start와 같음)<br>9장 1단계 (코드 14-2가 복사)<br>14장 [코드 14-3]<br>14장 [코드 14-4]<br>14장 '예시 답안 — 주간 업무 보고 흐름' 다음 코드<br>원고 밖 — 코드 14-2를 저자가 실행한 결과 (본문은 9장 inquiries_nov.txt) |
| 15장 업무 하나를 끝까지 분해하기 | `prompts/make-meetings.txt` — 회의록 만들기 요청<br>`weekly-meeting/meetings/2026-11-03.md`<br>`weekly-meeting/meetings/2026-11-10.md`<br>`prompts/design-review.txt` — 설계 검토 요청 | `design-v1.txt` — 설계서 v1 (처음 쓴 모양)<br>`weekly-meeting/design.md` — 설계서 v2 (P4-②)<br>`diy/expense-design.txt` — 혼자하기 예시 | 15장 [코드 15-1]<br>15장 [코드 15-3]<br>15장 [코드 15-2]<br>15장 [코드 15-4]<br>15장 '예시 답안 — 월말 경비 정산 확인 (재무 담당자)' 다음 코드 |
| 16장 주간 회의 후속 처리 완주하기 | — | `weekly-meeting/.claude/skills/meeting-followup/SKILL.md`<br>`weekly-meeting/.claude/skills/weekly-report/SKILL.md`<br>`weekly-meeting/.claude/skills/weekly-followup/SKILL.md`<br>`weekly-meeting/.claude/settings.json`<br>`finish-record.txt` — 첫 판 완주 기록 양식 (P4-⑤)<br>`diy/expense-file-map.txt` — 혼자하기 예시 | 2장 2단계 (2장 answers와 같음)<br>2장 혼자하기 예시 + 16장 1단계 '한 줄 고치기' 상자<br>16장 [코드 16-2]<br>16장 [코드 16-3]<br>16장 [코드 16-4]<br>16장 '예시 답안 — 월말 경비 정산 확인 (15장 예시 이어서)' 다음 코드 |

## 장별 메모

### 1장 AI 에이전트 시대의 변화 읽기

- 작업 폴더: `바탕화면 등 아무 곳 (3장부터 ~/Desktop/book-practice)`
- 세 방식(질문형·대화형·위임형)의 결과는 실행마다 달라서 싣지 않았습니다. 원고의 '예시 관찰 결과'를 참고하세요.

### 2장 Skill이란 무엇인가

- 작업 폴더: `바탕화면 (Skill 폴더) — Claude Desktop에 올릴 때는 폴더째 ZIP으로 압축`
- description 적중률 실험(표 2-3)의 결과는 실행마다 달라집니다.

### 3장 MCP란 무엇인가

- 작업 폴더: `~/Desktop/book-practice`
- followup_mail.md는 Claude가 만드는 결과라 싣지 않았습니다.
- start의 book-practice/weekly-notes/this_week.txt는 혼자하기 예시 답안이 읽는 '이번 주 업무 메모(연습용 사본)'의 꾸러미 전용 예시입니다. 원고에는 폴더 구성만 있습니다. 내 업무 메모의 연습용 사본이 있으면 그걸 쓰세요. 4장 혼자하기도 같은 파일을 씁니다.

### 4장 두 기술의 연결고리

- 작업 폴더: `~/Desktop/book-practice`
- draft_mail.md·review.md·final_mail.md는 실행마다 달라서 싣지 않았습니다. 원고 3단계 '저자가 해 본 결과' 상자를 참고하세요.

### 5장 첫 Skill 만들기

- 작업 폴더: `~/Desktop/book-skills (Skill 원본), ~/Desktop/book-practice/ch07 (실습 자료)`
- 혼자하기 예시(weekly-report 다듬기)는 원고에 바뀐 줄만 실려 있어 Skill 폴더 전체로 만들지 않았습니다. diy/weekly-report/references/report-format.md는 원고가 칸 이름(끝낸 일 / 진행 중 / 다음 주 계획 / 요청 사항)만 말한 양식의 꾸러미 전용 예시입니다. 2장 diy/weekly-report에 references/ 폴더째 더해 쓰세요.
- 테스트 표(표 5-3)의 결과는 실행마다 달라집니다.

### 6장 Skill 설계 원칙

- 작업 폴더: `~/Desktop/book-skills, ~/Desktop/book-practice/ch08`
- cs-helper는 진단용 예시입니다. 설치하지 말고 읽기만 하세요.

### 7장 실전 Skill 제작

- 작업 폴더: `~/Desktop/book-skills, ~/Desktop/book-practice/ch09`
- 월간 보고서 결과는 실행마다 달라집니다. 결과 점검표(표 7-2)로 확인하세요.
- 혼자하기 예시(meeting-agenda)는 원고에 폴더 구조와 확인 기준 세 줄만 실려 있습니다. diy/book-skills/의 meeting-agenda 폴더와 안내.txt는 꾸러미 전용 예시입니다(확인 기준 세 줄은 원고 그대로).
- 도전하기 challenge/inquiry-monthly-report/는 계산 스크립트를 넣은 뒤 바뀌는 파일만 담았습니다: SKILL.md(절차 3번을 원고 '방향 제시'의 문장으로 바꾸고 실행 방법 한 줄을 더함)와 scripts/calc_changes.py. answers의 inquiry-monthly-report 폴더에 덮어 쓰세요. calc_changes.py와 tests/는 꾸러미 전용 예시입니다.
- 스크립트 시험: challenge 폴더에서 python3 -m unittest discover tests (표준 라이브러리만 씀). 직접 실행: python3 inquiry-monthly-report/scripts/calc_changes.py 배송=18,11 교환·반품=9,10 환불=6,7 기타=4,5 "판단 필요=3,2" 합계=40,35

### 8장 Skill 디버깅과 개선

- 작업 폴더: `~/Desktop/book-skills`
- start의 customer-reply는 5장 Skill에 1단계 '동료가 바꾼 곳' 세 군데를 적용한 버그판입니다. 원본은 5장 answers에 있습니다.
- 디버깅을 마친 customer-reply는 5장 answers와 같아야 합니다.
- challenge/book-skills/건강검진.txt는 도전하기 '건강검진 세트'의 꾸러미 전용 예시입니다. 서랍의 Skill 네 개(meeting-followup, customer-reply, inquiry-classify, inquiry-monthly-report)와 그 사이의 경계 줄, Skill마다 가장 중요한 세 줄을 담았습니다.

### 9장 [복합 실습] 여러 Skill 조합 자동화

- 작업 폴더: `~/Desktop/book-skills, ~/Desktop/book-practice/ch11`
- 분류·보고서·답장 결과는 실행마다 달라집니다. 월말 흐름 점검표(표 9-2)로 확인하세요.

### 11장 기존 MCP 서버 연결해 보기

- 작업 폴더: `~/Desktop/book-reference`
- claude_desktop_config.json의 /Users/사용자이름 은 내 사용자 이름으로 바꾸세요. 이미 다른 설정이 있는 파일이면 통째로 덮어쓰지 말고 mcpServers 안의 덩어리만 더하세요(원고 코드 11-4).
- diy/claude_desktop_config.json은 코드 11-1에 코드 11-7(customer-memory)을 더한 모습입니다.

### 12장 나만의 MCP 서버 만들기 (기초)

- 작업 폴더: `~/book-code/inquiry-box`
- answers/ch12/inquiry-box는 원고가 '예제 저장소'라고 부르는 비교용 서버입니다(원고의 옛 경로 examples/ch14/inquiry-box). 테스트 16개, 샘플 문의 5통.
- Claude Code가 만드는 서버는 매번 조금씩 다릅니다. 3단계 점검표(표 12-5)를 통과하면 같은 서버입니다.
- diy/inquiry-box는 혼자하기 list_drafts 안내판대로 도구를 더한 서버의 꾸러미 전용 예시입니다(원고에는 안내판만 실림). answers/ch12/inquiry-box와 같은 서버에 list_drafts와 테스트 5개를 더했고, 그 폴더에서 uv run pytest -q로 21개 테스트가 돕니다.

### 13장 MCP 보안과 운영 고려사항

- 작업 폴더: `~/book-code/inquiry-box`
- 2026-11-006.txt는 숨은 지시를 일부러 넣은 연습용 문의입니다. 실습 뒤에는 지우거나 보관 폴더로 옮기세요.

### 14장 [복합 실습] Skill + 자작 MCP 서버 워크플로우

- 작업 폴더: `~/book-code/inquiry-box`
- answers의 inbox/2026-11/ 열두 통은 코드 14-2 요청을 저자가 실행한 결과입니다(받은 날 2026-11-07). 제목과 날짜는 여러분 실행에서 다를 수 있고, 본문은 9장 inquiries_nov.txt와 같아야 합니다.
- .claude/skills/의 customer-reply·inquiry-classify·inquiry-monthly-report는 5~7장 answers의 book-skills 폴더를 그대로 복사합니다.
- 보고서와 답장 초안은 실행마다 달라집니다. 흐름 기록 카드(코드 14-4)로 확인하세요.

### 15장 업무 하나를 끝까지 분해하기

- 작업 폴더: `~/book-code/weekly-meeting`
- start의 meetings/ 두 파일은 코드 15-1 요청문에 든 회의록을 그대로 나눈 것입니다. 요청을 붙여넣는 대신 복사해 써도 됩니다.
- 설계 검토(4단계) 결과는 실행마다 달라집니다.

### 16장 주간 회의 후속 처리 완주하기

- 작업 폴더: `~/book-code/weekly-meeting`
- weekly-report는 2장 예시 답안에서 '팀장님께'를 '본부장님께'로 바꾼 것입니다(1단계 상자).
- followup/2026-11-10.md와 reports/weekly-2026-11-10.md는 실행마다 달라집니다. 원고 5단계의 '확인 필요' 예와 확인 기준표(표 16-3)로 확인하세요.

## 꾸러미 전용 예시 (원고에는 구조만 있음)

책이 이름·위치·구조만 말하고 내용은 싣지 않은 파일입니다. 꾸러미에서 **가능한 답 하나**로 만들어 넣었습니다.
내 파일과 다르다고 틀린 것은 아닙니다. 책의 확인 기준과 테스트 표로 확인하세요.

| 장 | 꾸러미 위치 | 원고에서 |
|---|---|---|
| 3장 | `start/ch03/book-practice/weekly-notes/this_week.txt` | 원고 밖 — 3장 혼자하기 예시 답안의 폴더 구성에 이름만 나옴 |
| 5장 | `answers/ch05/diy/weekly-report/references/report-format.md` | 원고 밖 — 5장 혼자하기 예시 답안의 폴더 구성에 칸 이름만 나옴 |
| 7장 | `answers/ch07/challenge/inquiry-monthly-report/SKILL.md` | 7장 [코드 7-5] + 도전하기 '방향 제시'의 절차 3번 문장 (실행 방법 한 줄은 꾸러미에서 더함) |
| 7장 | `answers/ch07/diy/book-skills/meeting-agenda/` | 원고 밖 — 7장 혼자하기 예시 답안의 폴더 구조와 확인 기준 세 줄로 만듦 |
| 7장 | `answers/ch07/diy/book-skills/meeting-agenda-안내.txt` | 원고 밖 — 7장 혼자하기 예시 답안의 폴더 구조에 이름만 나옴 |
| 7장 | `answers/ch07/challenge/inquiry-monthly-report/scripts/` | 원고 밖 — 7장 도전하기의 폴더 구조에 이름과 역할만 나옴 |
| 7장 | `answers/ch07/challenge/tests/` | 원고 밖 — calc_changes.py 시험 (Skill 폴더 밖) |
| 8장 | `answers/ch08/challenge/book-skills/건강검진.txt` | 원고 밖 — 8장 도전하기 '방향 제시'로 만듦 |
| 12장 | `answers/ch12/diy/inquiry-box/` | 원고 밖 — 12장 예제 서버를 바탕으로 혼자하기 list_drafts 안내판대로 만듦 |
