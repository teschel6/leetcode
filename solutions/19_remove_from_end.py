# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

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
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None

        history = []
        node = head

        while node is not None:
            if len(history) == n + 1:
                history.pop(0)

            history.append(node)

            node = node.next

        # remove the first element in list
        if len(history) < n:
            raise ValueError(f"out of bounds, cannot remove {n} element from list")
        elif len(history) == n:
            head = head.next
        else:
            # get the nth element from end and previous
            remove_prev = history[-1 * (n + 1)]
            remove = history[-1 * n]

            # remove the nth element from end
            remove_prev.next = remove.next

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
    ([1, 2, 3, 4, 5], 2),
    ([1, 2, 3, 4, 5], 1),
    ([1, 2], 2),
    ([1], 1),
]

for l1, n in tests:
    head = link_list(l1)

    print(f"{head=}")

    removed = solution.removeNthFromEnd(head, n)

    print(f"{removed=}")
    print("=" * 24)
