import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice: int = sys.maxsize
        maxProfit = 0
        for e in prices:
            if e < minPrice:
                minPrice = e
            elif e - minPrice > maxProfit:
                maxProfit = e - minPrice
        return maxProfit
