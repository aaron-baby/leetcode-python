from unittest import TestCase

from zizzag_convertion import Solution


class TestSolution(TestCase):
    def test_convert(self):
        s = "PAYPALISHIRING"
        num_rows = 3
        self.assertEqual(Solution().convert(s, num_rows), "PAHNAPLSIIGYIR")
        num_rows = 4
        self.assertEqual(Solution().convert(s, num_rows), "PINALSIGYAHRPI")
        self.assertEqual(Solution().convert("A", 1), "A")
