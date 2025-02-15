class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def check_balance(self, root: TreeNode):
        if not root:
            return 0

        left = self.check_balance(root.left)
        right = self.check_balance(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        print(max(left, right))
        return max(left, right) + 1

    def isBalanced(self, root):
        return self.check_balance(root) != -1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(9)

sol = Solution()
print(sol.isBalanced(root))