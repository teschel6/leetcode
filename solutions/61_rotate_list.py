# https://leetcode.com/problems/rotate-list/description/

from typing import List


# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        node = self
        repr = ""
        while node is not None:
            repr += f"{node.val}->"
            node = node.next

        return repr


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None

        node = head
        prev = None
        length = 0

        while node is not None:
            prev = node
            node = node.next
            length += 1

        tail = prev
        k = k % length

        if k == 0:
            return head

        node = head
        prev = None
        rotate = None
        rotate_point = length - k
        i = 0

        while node is not None:
            if i == rotate_point:
                rotate = node
                break

            prev = node
            node = node.next
            i += 1

        if tail and prev:
            tail.next = head
            prev.next = None

        return rotate


def link_list(list: List[int]) -> ListNode:
    """Create a linked list returns head node"""
    if list is None:
        return None

    node = ListNode()
    next = None

    for val in reversed(list):
        node = ListNode(val, next)
        next = node

    return node


solution = Solution()

tests = [
    ([1, 2, 3, 4, 5], 1),
    ([1, 2, 3, 4, 5], 2),
    ([1, 2, 3, 4, 5], 6),
    ([0, 1, 2], 1),
    ([0, 1, 2], 2),
    ([0, 1, 2], 3),
    ([0, 1, 2], 4),
    ([0, 1, 2], 5),
    (None, 5),
]

for lst, k in tests:
    head = link_list(lst)

    rotated = solution.rotateRight(head, k)

    print(f"{head=}")
    print(f"{k=}")
    print(f"{rotated=}")
    print("=" * 12)
