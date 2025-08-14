# https://leetcode.com/problems/add-two-numbers/description/

from typing import List


# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sum_list = []
        carry = False

        # sum the lists
        while l1 is not None or l2 is not None:
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            sum = val1 + val2 + (1 if carry else 0)
            carry = sum >= 10
            sum = sum % 10

            # save result
            sum_list.append(sum)

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        # add the final carry
        if carry:
            sum_list.append(1)

        return self.link_list(sum_list)

    def link_list(self, list: List[int]) -> ListNode:
        """Create a linked list returns head node"""

        node = ListNode()
        next = None

        for val in reversed(list):
            node = ListNode(val, next)
            next = node

        return node


def list_str(list: ListNode | None):
    """Print out element in linked list."""
    str = ""
    while list is not None:
        str += f"{list.val}->"
        list = list.next

    return str


solution = Solution()

tests = [
    ([2, 4, 3], [5, 6, 4]),
    ([0, 5], [0, 5]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]),
    ([0], [0]),
    ([], [0]),
    ([], []),
]

for a, b in tests:
    a = solution.link_list(a)
    b = solution.link_list(b)
    sum = solution.addTwoNumbers(a, b)

    print("b = " + list_str(a))
    print("a = " + list_str(b))
    print("sum = " + list_str(sum))
