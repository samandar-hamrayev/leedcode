# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def exists(index, level, root):
            left, right = 0, 2 ** level - 1
            node = root
            for _ in range(level):
                mid = (left+right) // 2
                if index <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return node is not None

        if not root:
            return 0

        left_depth = 0
        right_depth = 0
        left_node = root
        right_node = root

        while left_node:
            left_depth += 1
            left_node = left_node.left

        while right_node:
            right_depth += 1
            right_node = right_node.right

        if left_depth == right_depth:
            return 2 ** left_depth - 1

        low, high = 0, 2 ** (left_depth - 1) - 1
        while low <= high:
            mid = (low + high) // 2
            if exists(mid, left_depth - 1, root):
                low = mid + 1
            else:
                high = mid - 1

        return (2 ** (left_depth - 1) - 1) + low

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
sol = Solution()
print(sol.countNodes(root))




