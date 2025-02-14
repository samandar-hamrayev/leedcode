from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        def generate_tree(start, end):
            if start > end:
                return [None, ]

            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate_tree(start, i - 1)
                right_trees = generate_tree(i + 1, end)

                for l in left_trees:
                    for r in right_trees:
                        curr = TreeNode(i)
                        curr.left = l
                        curr.right = r
                        all_trees.append(curr)

        return generate_tree(1, n) if n else []


