"""실행: 이 폴더(challenge)에서 python3 -m unittest discover tests"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "inquiry-monthly-report" / "scripts" / "calc_changes.py"
sys.path.insert(0, str(SCRIPT.parent))

from calc_changes import InputError, Row, change, parse_arg, rate, render

NOVEMBER = ["배송=18,11", "교환·반품=9,10", "환불=6,7", "기타=4,5", "판단 필요=3,2"]


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True, check=False)


class CalcChangesTest(unittest.TestCase):
    def test_november_matches_result_checklist_r2(self):
        """표 7-2 R2의 기대값과 같은 증감이 나오고, 표는 템플릿처럼 네 칸이다."""
        out = render(NOVEMBER)
        table = out.split("\n\n")[0].splitlines()
        self.assertEqual(len(table), 7)  # 머리 줄 + 유형 다섯 줄 + 합계 줄
        self.assertTrue(all(line.count(" | ") == 3 for line in table))
        for expected in [
            "배송 | 11 | 18 | +7 (18−11)",
            "교환·반품 | 10 | 9 | −1 (9−10)",
            "환불 | 7 | 6 | −1 (6−7)",
            "기타 | 5 | 4 | −1 (4−5)",
            "판단 필요 | 2 | 3 | +1 (3−2)",
            "합계 | 35 | 40 | +5 (40−35)",
        ]:
            with self.subTest(expected=expected):
                self.assertIn(expected, out)

    def test_rate_has_sign_and_one_decimal(self):
        self.assertEqual(rate(Row("배송", 18, 11)), "+63.6%")
        self.assertEqual(rate(Row("환불", 6, 7)), "−14.3%")
        self.assertEqual(rate(Row("같음", 5, 5)), "0.0%")
        self.assertEqual(change(Row("같음", 5, 5)), "0 (5−5)")

    def test_last_month_zero_or_unknown(self):
        self.assertEqual(rate(Row("판단 필요", 3, 0)), "계산 안 함 (지난달 0건)")
        self.assertEqual(change(Row("판단 필요", 3, 0)), "+3 (3−0)")
        out = render(["배송=18,11", "기타=4,"])
        self.assertIn("기타 | 확인 필요 | 4 | 확인 필요\n", out)
        self.assertIn("합계 | 확인 필요 | 22 | 확인 필요\n", out)
        self.assertIn("기타: 확인 필요", out)

    def test_total_check(self):
        self.assertIn("합계 확인: 입력 합계와 같음", render([*NOVEMBER, "합계=40,35"]))
        wrong = render([*NOVEMBER, "합계=41,35"])
        self.assertIn("합계 확인: 확인 필요 (이번 달 입력 41 / 계산 40)", wrong)

    def test_bad_input(self):
        for bad in ["배송", "배송=열여덟,11", "배송=-1,3", "=3,2", "배송=1.5,2", "배송=²,1"]:
            with self.subTest(bad=bad), self.assertRaises(InputError):
                parse_arg(bad)
        with self.assertRaises(InputError):
            render(["배송=1,2", "배송=3,4"])
        with self.assertRaises(InputError):
            render([])

    def test_cli_stdout_and_exit_codes(self):
        ok = run(*NOVEMBER, "합계=40,35")
        self.assertEqual(ok.returncode, 0)
        self.assertTrue(ok.stdout.startswith("유형 | 지난달 | 이번 달 | 증감 (계산식)\n"))
        self.assertIn("배송: +63.6%", ok.stdout)
        self.assertEqual(ok.stderr, "")
        bad = run("배송=많음,11")
        self.assertEqual(bad.returncode, 2)
        self.assertEqual(bad.stdout, "")  # 오류는 stdout을 더럽히지 않는다
        self.assertIn("입력 오류", bad.stderr)


if __name__ == "__main__":
    unittest.main()
