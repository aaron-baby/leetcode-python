# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # two pointer, cur point to kth element
        #     rev point to kth element from the end
        pre, curr = dummy, head

        while k - 1 > 0:
            pre = curr
            curr = curr.next
            k -= 1
        # print(pre.val, curr.val)
        rev_pre, rev = dummy, head
        curr_copy = curr
        while curr_copy.next:
            rev_pre = rev
            rev = rev.next
            curr_copy = curr_copy.next
        # save ptrs
        rev_next = rev.next

        # if curr's next node is rev, then rev node point to curr, otherwise, rev node point to curr's next node
        # if rev's next node is curr, then curr node point to rev.
        if curr.next == rev:
            rev.next = curr
            curr.next = rev_next
            pre.next = rev
        elif rev.next == curr:
            curr_next = curr.next
            curr.next = rev
            rev.next = curr_next
            rev_pre.next = curr
        else:
            rev.next = curr.next
            pre.next = rev
            curr.next = rev_next
            rev_pre.next = curr

        return dummy.next
