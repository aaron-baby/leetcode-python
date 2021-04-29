import unittest

from spiral_matrix import Solution


class TestSolution(unittest.TestCase):
    def test_spiral_order(self):
        s = Solution()
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(s.spiralOrder(matrix), [1, 2, 3, 6, 9, 8, 7, 4, 5])

        m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        self.assertEqual(s.spiralOrder(m2), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])

        m3 = [[3], [2]]
        self.assertEqual(s.spiralOrder(m3), [3, 2])
