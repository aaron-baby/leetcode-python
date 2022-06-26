from unittest import TestCase, skip

from linked_list.swapping_nodes_in_a_linked_list import Solution
from tests.util import convert_value_to_linked_list, get_result_list


class TestSolution(TestCase):
    def test_swap_nodes(self):
        head = [1, 2, 3, 4, 5]
        k = 2
        nodes = convert_value_to_linked_list(head)
        h = Solution().swapNodes(nodes, k)
        self.assertEqual(get_result_list(h), [1, 4, 3, 2, 5])

        # print("\n===test2===\n")
        head = [7, 9, 6, 6, 7, 8, 3, 0, 9, 5]
        k = 6
        nodes = convert_value_to_linked_list(head)
        h = Solution().swapNodes(nodes, k)
        self.assertEqual(get_result_list(h), [7,9,6,6,8,7,3,0,9,5])

