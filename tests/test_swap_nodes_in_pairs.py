from unittest import TestCase

from linked_list.swap_nodes_in_pairs import Solution
from tests.util import convert_value_to_linked_list, get_result_list


class TestSolution(TestCase):
    def test_swap_pairs(self):
        head = [1,2,3,4]
        nodes = convert_value_to_linked_list(head)
        h = Solution().swapPairs(nodes)
        self.assertEqual(get_result_list(h), [2, 1, 4, 3])
