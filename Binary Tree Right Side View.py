# Definition for a binary tree node.
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    def rightSideView_2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = {1: root.val}

        queue = deque()
        queue.append((root, 1))
        while queue:
            node, level = queue.popleft()

            if node.right is not None:
                queue.append((node.right, level + 1))
                if (level + 1) not in result:
                    result[level + 1] = node.right.val

            if node.left is not None:
                queue.append((node.left, level + 1))
                if (level + 1) not in result:
                    result[level + 1] = node.left.val

        return list(result.values())



root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)

sol = Solution()
print(sol.rightSideView(root))


