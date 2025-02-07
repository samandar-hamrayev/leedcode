# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def with_dfs(self, root: Optional[TreeNode]) -> list[int]:
        ans = []
        def dfs(root: TreeNode):
            if not root:
                return

            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return ans

    def iterativ(self, root: TreeNode):
        res, stack = [], []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.val)
            current = current.right
        return res

    def while_tsikl(self, root: TreeNode):
        result, stack = [], []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right

        return result


# daraxt yaratish
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

# daraxt ustidagi amallar
sol = Solution()
print(sol.with_dfs(root))





