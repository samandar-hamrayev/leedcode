# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, -float('inf'), float('inf'))])

        while q:
            node, min_val, max_val = q.popleft()

            if not (min_val < node.val < max_val):
                return False

            if node.left:
                q.append((node.left, min_val, node.val))
            if node.right:
                q.append((node.right, node.val, max_val))

        return True

    def isValidBST_2(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True

            if not (min_val < node.val < max_val):
                return False

            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

        return validate(root, float('-inf'), float('inf'))



root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)
root.right.left = TreeNode(3)  # Bu BST shartlarini buzadi
root.right.right = TreeNode(8)

sol = Solution()
print(sol.isValidBST(root))


