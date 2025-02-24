# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.mindiff = float('inf')
        self.prev = None
        def dfs(node: TreeNode):
            if not node:
                return

            dfs(node.left)

            if self.prev is not None:
                self.mindiff = min(self.mindiff, node.val - self.prev)
            self.prev = node.val
            dfs(node.right)
        dfs(root)
        return self.mindiff




root = TreeNode(100000, TreeNode(0))
# root.left = TreeNode(0)
# root.right = TreeNode(48)
# root.right.left = TreeNode(12)
# root.right.right = TreeNode(49)


sol = Solution()
print(sol.getMinimumDifference(root))
