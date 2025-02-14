# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        q = deque([(root.left, root.right)])
        while q:
            node1, node2 = q.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            q.append((node1.left, node2.right))
            q.append((node1.right, node2.left))
        return True



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

sol = Solution()
print(sol.isSymmetric(root))
