# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bst(nums):
            if not nums:
                return None

            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left, root.right = bst(nums[:mid]), bst(nums[mid+1:])
            return root
        return bst(nums)

sol = Solution()
print(sol.sortedArrayToBST(nums = [-10,-3,0,5,9]))

