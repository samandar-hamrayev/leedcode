from typing import Optional, List

from Combinations import solution


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Daraxt yaratish
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)

root.left.left = TreeNode(1)
root.left.right = TreeNode(4)

root.right.left = TreeNode(7)
root.right.right = TreeNode(10)

root.left.left.left = TreeNode(0)
root.right.left.right = TreeNode(6)
root.right.right.left = TreeNode(9)


# """
#         5
#        / \
#       3   8
#      / \  / \
#     1   4 7  10
#    /      \  /
#   0        6 9
# """


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return  []

        result, stack = [], [root]
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return result

sol = Solution()
print(sol.preorderTraversal(root))




