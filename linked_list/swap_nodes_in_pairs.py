
from typing import Optional

from linked_list.util import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # always point to head
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            # save ptrs
            next_pair = curr.next.next
            second = curr.next

            # reverse node
            second.next = curr
            curr.next = next_pair
            prev.next = second

            # update ptrs
            prev = curr
            curr = next_pair
        return dummy.next
