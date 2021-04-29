# add alias
List = list


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        if rows == 0:
            return []
        cols = len(matrix[0])
        u, d = 0, rows - 1
        l, r = 0, cols - 1
        res = []
        while u <= d and l <= r:
            # top row, from l -> r
            for col in range(l, r + 1):
                res.append(matrix[u][col])
            u += 1
            if u > d:
                break
            # right col, from u+1 -> d
            for row in range(u, d + 1):
                res.append(matrix[row][r])
            r -= 1
            if r < l:
                break
            # bottom row, from r-1 -> l+1
            for col in range(r, l-1, -1):
                res.append(matrix[d][col])
            d -= 1
            if d < u:
                break
            # left col, from d -> u+1
            for row in range(d, u-1, -1):
                res.append(matrix[row][l])
            l += 1
            if l > r:
                break

        return res
