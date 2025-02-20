from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
from typing import Optional


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q = deque([root])

        while q:
            level_size = len(q)
            prev = None
            for _ in range(level_size):
                node = q.popleft()
                if prev:
                    prev.next = node
                prev = node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            prev.next = None
        return root



