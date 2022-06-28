class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        #### [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
        (you may want to display this pattern in a fixed font for better legibility)

        And then read line by line: "PAHNAPLSIIGYIR"
        Write the code that will take a string and make this conversion given a number of rows:
        """
        if numRows == 1:
            return s
        # create a list of lists
        rows = [[] for _ in range(numRows)]

        for i, c in enumerate(s):
            # n(0..n-1) rows down, then n-2 rows up(n..n[down length] + n-2[up length] - 1[start index]).
            remainder = i % (numRows * 2 - 2)
            if remainder < numRows:
                rows[remainder].append(c)
            else:
                # go up direction
                rows[numRows - 1 - (remainder - numRows + 1)].append(c)
        # print(rows)
        # join the rows
        return ''.join([''.join(row) for row in rows])
