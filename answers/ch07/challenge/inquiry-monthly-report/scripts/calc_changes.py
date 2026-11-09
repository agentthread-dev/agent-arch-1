"""유형별 이번 달·지난달 문의 건수를 받아 증감과 합계를 계산한다.

사용법 (유형마다 "유형=이번달,지난달"):
    python3 scripts/calc_changes.py 배송=18,11 교환·반품=9,10 환불=6,7 기타=4,5 "판단 필요=3,2"

선택: 입력 자료에 적힌 합계를 "합계=이번달,지난달"로 함께 주면, 계산한 합계와 같은지 확인한다.
    python3 scripts/calc_changes.py 배송=18,11 … 합계=40,35

지난달 건수를 모르면 "기타=4,"처럼 비워 둔다. 그 유형과 합계의 증감은 "확인 필요"가 된다.
유형 이름에 띄어쓰기가 있으면 인자 전체를 따옴표로 감싼다.

출력 (앞부분은 보고서 템플릿 2번 표와 같은 네 칸, 증감은 "이번 달 − 지난달"):
    유형 | 지난달 | 이번 달 | 증감 (계산식)
    배송 | 11 | 18 | +7 (18−11)
    …
    합계 | 35 | 40 | +5 (40−35)
    합계 확인: 입력 합계와 같음

    증감률 (지난달 대비, 문장에 쓸 때만 — 표에 칸을 더하지 않는다)
    배송: +63.6%
    …

입력이 잘못되면 stderr에 이유를 쓰고 종료 코드 2로 끝난다. 표준 라이브러리만 쓴다.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass

MINUS = "−"  # 보고서 표와 같은 빼기 기호 (U+2212)
UNKNOWN = "확인 필요"
TOTAL_NAME = "합계"


class InputError(ValueError):
    pass


@dataclass(frozen=True)
class Row:
    name: str
    this_month: int
    last_month: int | None  # None = 지난달 건수를 모름


def _count(text: str, name: str, which: str) -> int:
    text = text.strip()
    if not (text.isascii() and text.isdigit()):
        raise InputError(f"{name}의 {which} 건수가 0 이상의 정수가 아닙니다: {text!r}")
    return int(text)


def parse_arg(arg: str) -> Row:
    """'배송=18,11' → Row('배송', 18, 11). 지난달이 비어 있으면 last_month=None."""
    name, sep, numbers = arg.partition("=")
    name = name.strip()
    if not sep or not name:
        raise InputError(f"'유형=이번달,지난달' 모양이 아닙니다: {arg!r}")
    this_text, comma, last_text = numbers.partition(",")
    this_month = _count(this_text, name, "이번 달")
    last_month = _count(last_text, name, "지난달") if comma and last_text.strip() else None
    return Row(name, this_month, last_month)


def _fmt_signed(n: int) -> str:
    if n > 0:
        return f"+{n}"
    if n < 0:
        return f"{MINUS}{-n}"
    return "0"


def change(row: Row) -> str:
    """증감 칸: '+7 (18−11)'. 지난달을 모르면 '확인 필요'."""
    if row.last_month is None:
        return UNKNOWN
    diff = row.this_month - row.last_month
    return f"{_fmt_signed(diff)} ({row.this_month}{MINUS}{row.last_month})"


def rate(row: Row) -> str:
    """증감률: 지난달 대비 %, 소수 첫째 자리. 지난달이 0이거나 모르면 계산하지 않는다."""
    if row.last_month is None:
        return UNKNOWN
    if row.last_month == 0:
        return "계산 안 함 (지난달 0건)"
    pct = (row.this_month - row.last_month) / row.last_month * 100
    text = f"{abs(pct):.1f}%"
    if round(pct, 1) > 0:
        return f"+{text}"
    if round(pct, 1) < 0:
        return f"{MINUS}{text}"
    return "0.0%"


def total(rows: list[Row]) -> Row:
    this_month = sum(r.this_month for r in rows)
    known = all(r.last_month is not None for r in rows)
    last_month = sum(r.last_month for r in rows if r.last_month is not None) if known else None
    return Row(TOTAL_NAME, this_month, last_month)


def check_total(computed: Row, given: Row) -> str:
    """입력 자료의 합계와 계산한 합계를 비교한다. 다르면 표를 고치지 말라는 뜻으로 '확인 필요'."""
    problems = []
    if given.this_month != computed.this_month:
        problems.append(f"이번 달 입력 {given.this_month} / 계산 {computed.this_month}")
    if given.last_month is not None and computed.last_month is not None and given.last_month != computed.last_month:
        problems.append(f"지난달 입력 {given.last_month} / 계산 {computed.last_month}")
    if problems:
        return f"합계 확인: {UNKNOWN} ({', '.join(problems)})"
    return "합계 확인: 입력 합계와 같음"


def render(args: list[str]) -> str:
    rows: list[Row] = []
    given_total: Row | None = None
    for arg in args:
        row = parse_arg(arg)
        if row.name == TOTAL_NAME:
            given_total = row
        elif any(r.name == row.name for r in rows):
            raise InputError(f"같은 유형이 두 번 나옵니다: {row.name}")
        else:
            rows.append(row)
    if not rows:
        raise InputError("유형을 하나 이상 주세요. 예: 배송=18,11")
    computed = total(rows)
    lines = ["유형 | 지난달 | 이번 달 | 증감 (계산식)"]
    for row in [*rows, computed]:
        last = UNKNOWN if row.last_month is None else str(row.last_month)
        lines.append(f"{row.name} | {last} | {row.this_month} | {change(row)}")
    if given_total is not None:
        lines.append(check_total(computed, given_total))
    lines += ["", "증감률 (지난달 대비, 문장에 쓸 때만 — 표에 칸을 더하지 않는다)"]
    lines += [f"{row.name}: {rate(row)}" for row in [*rows, computed]]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    try:
        sys.stdout.write(render(args))
    except InputError as err:
        print(f"입력 오류: {err}", file=sys.stderr)
        print("사용법: python3 scripts/calc_changes.py 배송=18,11 교환·반품=9,10 …", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
