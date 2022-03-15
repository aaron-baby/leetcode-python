from unittest import TestCase

from pairs_of_songs_with_total_durations_divisible_by_60 import Solution


class TestSolution(TestCase):
    def test_num_pairs_divisible_by60(self):
        s = Solution()
        time = [30, 20, 150, 100, 40]
        self.assertEqual(s.numPairsDivisibleBy60(time), 3)
        time2 = [60, 60, 60]
        self.assertEqual(s.numPairsDivisibleBy60(time2), 3)
        time3 = [174,188,377,437,54,498,455,239,183,347,59,199,52,488,147,82]
        self.assertEqual(s.numPairsDivisibleBy60(time3), 2)