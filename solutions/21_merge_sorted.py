# https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import List


# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None:
            return None

        merged = []
        while list1 is not None or list2 is not None:
            if list1 is not None:
                merged.append(list1.val)
                list1 = list1.next

            if list2 is not None:
                merged.append(list2.val)
                list2 = list2.next

        return self.linkList(sorted(merged))

    def linkList(self, list: List[int]) -> ListNode:
        """Create a linked list returns head node"""

        node = ListNode()
        next = None

        for val in reversed(list):
            node = ListNode(val, next)
            next = node

        return node


def printList(list: ListNode | None):
    while list is not None:
        print(f"{list.val=}")
        list = list.next


tests = [
    ([1, 2, 4], [1, 3, 4]),
    ([], []),
    ([0], []),
]

solution = Solution()

for a, b in tests:
    a = solution.linkList(a)
    b = solution.linkList(b)

    merged = solution.mergeTwoLists(a, b)

    printList(merged)
