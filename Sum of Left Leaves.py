from typing import Optional



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, is_left: bool = False):
            if not node:
                return 0
            if not node.left and not node.right and is_left:
                return  node.val
            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root)




root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


sol = Solution()
print(sol.sumOfLeftLeaves(root))
