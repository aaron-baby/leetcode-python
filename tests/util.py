from linked_list.util import ListNode


def get_result_list(h):
    result = []
    while h is not None:
        result.append(h.val)
        h = h.next
    return result


def convert_value_to_linked_list(vals):
    next_node = None
    for v in reversed(vals):
        n = ListNode(v, next=next_node)
        next_node = n
    return n