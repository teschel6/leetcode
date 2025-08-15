# https://leetcode.com/problems/reverse-linked-list-ii/

from typing import List, Optional


# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left > right:
            raise ValueError("left must be lte right")
        elif left == right:
            return head

        if head is None:
            return None

        lnode = None
        rnode = None
        curr = head
        count = 1  # No, I don't like this either
        vals = []

        # get left node, right node, and vals
        while (lnode is None or rnode is None) and curr is not None:
            if count == left:
                lnode = curr

            if count == right:
                rnode = curr

            if count >= left and count <= right:
                vals.append(curr.val)

            # unexpected end of list
            if curr.next is None and count < right:
                raise ValueError(
                    f"Right index {right} is out of  bounds of list length {count}"
                )

            curr = curr.next
            count += 1

        # reverse the section
        rev_tail = None
        rev_curr = None
        rev_next = None

        for val in vals:
            rev_curr = ListNode(val, rev_next)

            # save the tail for later
            if rev_next is None:
                rev_tail = rev_curr

            rev_next = rev_curr

        rev_head = rev_curr

        # give it the razzle dazzle
        lnode.val = rev_head.val
        lnode.next = rev_head.next
        rev_tail.next = rnode.next

        return head


def link_list(list: List[int]) -> ListNode:
    """Create a linked list returns head node"""

    node = ListNode()
    next = None

    for val in reversed(list):
        node = ListNode(val, next)
        next = node

    return node


def list_str(list: ListNode | None):
    """Print out elements in linked list."""
    str = ""
    while list is not None:
        str += f"{list.val}->"
        list = list.next

    return str


solution = Solution()

tests = [
    ([1, 2, 3, 4, 5], 2, 4),
    ([1, 2, 3], 2, 3),
    ([1, 2], 2, 2),
    ([5], 1, 1),
]

for list, left, right in tests:
    list = link_list(list)

    print("list = " + list_str(list))

    rev_list = solution.reverseBetween(list, left, right)
    print("rev_list= " + list_str(rev_list))
