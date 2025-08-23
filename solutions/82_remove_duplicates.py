# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

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
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = head
        prev = None
        remove_later = set()

        while node is not None:
            if prev and prev.val == node.val:
                remove_later.add(prev.val)

            prev = node
            node = node.next

        node = head
        prev = None

        while node is not None:
            if node.val in remove_later:
                if prev is not None:
                    prev.next = node.next
                    node = prev
                else:
                    head = node.next
                    node = head
                    prev = None
                    continue

            prev = node
            node = node.next

        return head


def link_list(list: List[int]) -> ListNode:
    """Create a linked list returns head node"""

    node = ListNode()
    next = None

    for val in reversed(list):
        node = ListNode(val, next)
        next = node

    return node


solution = Solution()

tests = [
    [1, 1, 1, 2, 3],
    [1, 2, 2, 3],
    [1, 2, 2, 3, 3],
    [1, 2, 3, 3, 4, 4, 5],
    [1, 1, 2, 2, 2, 2],
    [1, 2],
    [1],
]

for test in tests:
    head = link_list(test)

    print(f"{head=}")

    removed = solution.deleteDuplicates(head)
    print(f"{removed=}")
    print("=" * 24)
