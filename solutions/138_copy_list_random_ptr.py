# https://leetcode.com/problems/copy-list-with-random-pointer/description

from typing import List, Tuple
from typing import Optional


# Definition for singly-linked list with
class ListNode(object):
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def __repr__(self):
        node = self
        repr = ""
        while node is not None:
            if node.random is not None:
                if isinstance(node.random, ListNode):
                    random = node.random.val
                elif isinstance(node.random, int):
                    random = f"[{node.random}]"
                else:
                    random = "unknown"
            else:
                random = None

            repr += f"{node.val}({random})->"
            node = node.next

        return repr


class Solution:
    def copyRandomList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return head


def link_list(list: List[Tuple]) -> ListNode:
    """Create a linked list returns head node"""
    if list is None:
        return None

    node = ListNode()
    next = None

    indexed = []

    for val, rand_index in reversed(list):
        node = ListNode(val, next, rand_index)
        next = node
        indexed.insert(0, node)

    head = node

    # link random ptr based on index
    while node is not None:
        index = node.random
        if index is not None:
            node.random = indexed[index]
        node = node.next

    return head


solution = Solution()

tests = [
    [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)],
]

for lst in tests:
    head = link_list(lst)
    print(f"{head=}")
