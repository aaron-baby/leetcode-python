from unittest import TestCase

from best_time_to_buy_and_sell_stock import Solution

class TestSolution(TestCase):
    def test_max_profit(self):
        self.assertEqual(Solution.maxProfit(self, [7,1,5,3,6,4]), 5)
        self.assertEqual(Solution.maxProfit(self, [7,6,4,3,1]), 0)
