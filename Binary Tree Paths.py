from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(root, path):
            if not root:
                return
            path.append(str(root.val))
            if not root.right and not root.left:
                result.append("->".join(path))
            else:
                dfs(root.left, path)
                dfs(root.right, path)
            path.pop()
        dfs(root, [])
        return result


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
print(sol.binaryTreePaths(root))