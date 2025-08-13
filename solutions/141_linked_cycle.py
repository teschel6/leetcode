# https://leetcode.com/problems/linked-list-cycle/description/

from typing import List


# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        node = head

        while node is not None:
            if node in visited:
                return True

            visited.add(node)

            node = node.next

        return False


def print_list(list: ListNode | None, max: int = 10):
    """Print out element in linked list.

    - limit output to max in-case of cycles in list
    """
    count = 0

    while list is not None:
        print(f"{list.val=}")
        list = list.next

        if count >= max:
            break

        count += 1


def link_list_with_cycle(list: List, cycle_pos: int | None):
    """Create a linked list returns head node"""

    node = ListNode()
    next = None

    # create the linked list
    for val in reversed(list):
        node = ListNode(val, next)
        next = node

    head = node

    if cycle_pos is None:
        return head

    # find the cycle and tail nodes
    cycle = None
    tail = None
    pos = 0

    while node is not None:
        if pos == cycle_pos:
            cycle = node

        if node.next is None:
            tail = node

        node = node.next
        pos += 1

    # link the cycle node
    if tail:
        tail.next = cycle
    else:
        raise ValueError("tail node not found")

    return head


solution = Solution()

tests = [
    ([3, 2, 0, -4], 1),
    ([1, 12, 3, 5, 3], 3),
    ([1, 2], 1),
    ([1, 5, 3], None),
    ([1], None),
]

for list, cycle_pos in tests:
    head = link_list_with_cycle(list, cycle_pos)

    has_cycle = solution.hasCycle(head)
    print(f"{has_cycle=}")
