# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, path, remaining):
            if not node:
                return
            path.append(node.val)

            if not node.left and not node.right and remaining == node.val:
                res.append(path[:])
            dfs(node.left, path, remaining - node.val)
            dfs(node.right, path, remaining - node.val)
            path.pop()
        dfs(root, [], targetSum)
        return res
root = TreeNode(1)
root.right = TreeNode(2)
sol = Solution()
print(sol.pathSum(root, 3))


