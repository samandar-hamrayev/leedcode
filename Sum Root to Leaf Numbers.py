# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, path_sum):
            if not node:
                return None
            path_sum = path_sum * 10 + node.val
            if not node.left and not node.right:
                return path_sum

            return dfs(node.left, path_sum) + dfs(node.right, path_sum)
        return dfs(root, 0)


root = TreeNode(4)
root.left = TreeNode(9)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
root.right = TreeNode(0)

sol = Solution()
print(sol.sumNumbers(root))