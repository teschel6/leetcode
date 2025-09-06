# https://leetcode.com/problems/partition-list/

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
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        lt_head = None
        gte_head = None

        lt_tail = None
        gte_tail = None

        node = head

        while node is not None:
            if node.val < x:
                lt_head, lt_tail = self.add_node(
                    head=lt_head,
                    tail=lt_tail,
                    val=node.val,
                )
            elif node.val >= x:
                gte_head, gte_tail = self.add_node(
                    head=gte_head,
                    tail=gte_tail,
                    val=node.val,
                )

            node = node.next

        print(f"{lt_head=}")
        print(f"{gte_head=}")

        if lt_tail and gte_head:
            lt_tail.next = gte_head

        return lt_head

    def add_node(self, head, tail, val):
        """add node to end of list"""
        if head is None:
            head = ListNode(val, None)
            tail = head
        else:
            tail.next = ListNode(val, None)
            tail = tail.next

        return (head, tail)


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
    ([1, 4, 3, 2, 5, 2], 3),
    ([2, 1], 2),
    ([1], 0),
    (None, 0),
]

for lst, x in tests:
    head = link_list(lst)

    partitioned = solution.partition(head, x)

    print(f"{head=}")
    print(f"{x=}")
    print(f"{partitioned=}")
    print("=" * 24)
