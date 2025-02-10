# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        queue = deque()
        queue.append((root, root.val))
        while queue:
            len_queue = len(queue)

            for _ in range(len_queue):
                node, till_max = queue.popleft()

                if node.val >= till_max:
                    till_max = node.val
                    count += 1
                if node.right is not None:
                    queue.append((node.right, till_max))

                if node.left is not None:
                    queue.append((node.left, till_max))
        return count

root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.right = TreeNode(4)
root.right.right = TreeNode(5)
root.right.left = TreeNode(1)

sol = Solution()
print(sol.goodNodes(root))

