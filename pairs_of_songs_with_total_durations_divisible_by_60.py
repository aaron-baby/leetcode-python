# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
from collections import defaultdict

import math
from typing import TypeAlias

List: TypeAlias = list


class Solution:
    def numPairsDivisibleBy60_tle(self, time: List[int]) -> int:
        cnt = 0
        l = len(time)
        for i in range(l):
            n = i + 1
            for j in range(n, l):
                # print("p:", i, j)
                if (time[i] + time[j]) % 60 == 0:
                    cnt += 1
        return cnt

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = 0
        # (1, 59), (2, 58)
        rem2count = defaultdict(int)
        for i in range(len(time)):
            # we want to know that, for each t,
            # how many x satisfy (t + x) % 60 = 0.
            # The straight forward idea is to take x % 60 = 60 - t % 60
            # 取模之后的余数
            rem = time[i] % 60
            # pair mode
            if rem == 0:
                cnt += rem2count[0]
            else:
                cnt += rem2count[60 - rem]
            rem2count[rem] += 1
        return cnt


if __name__ == "__main__":
    Solution().numPairsDivisibleBy60([1, 2])
