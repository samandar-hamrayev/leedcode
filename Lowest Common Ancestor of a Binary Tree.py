# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traversal(node: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
            if not node or node.val == p.val or node.val == q.val:
                return node

            left = traversal(node.left, p, q)
            right = traversal(node.right, p, q)
            if left and right:
                return node
            return left if left else right
        return traversal(root, p, q)

    def iterative_way_for_solution(self, root: TreeNode, p: TreeNode, q: TreeNode):
        if not root:
            return None
        parent = {root: None}
        stack = [root]
        while p not in parent or q not in parent:
            node = stack.pop(0)
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set()
        while parent[q]:
            ancestors.add(q)
            q = parent[q]

        while p not in ancestors:
            p = parent[p]
        return p


root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

sol = Solution()
print(sol.iterative_way_for_solution(root, root.left, root.left.right).val)

