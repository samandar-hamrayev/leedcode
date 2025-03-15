# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        current_count = 0
        max_count = 0
        modes = []
        prev_val = None
        current = root
        while current:
            if current.left is None:
                if prev_val == current.val:
                    current_count += 1
                else:
                    current_count = 1

                if current_count > max_count:
                    max_count = current_count
                    modes = [current.val]
                elif current_count == max_count:
                    modes.append(current.val)

                prev_val = current.val
                current = current.right
            else:
                prev = current.left
                while prev.right and prev.right != current:
                    prev = prev.right

                if prev.right is None:
                    prev.right = current
                    current = current.left
                else:
                    prev.right = None

                    if prev_val == current.val:
                        current_count += 1
                    else:
                        current_count = 1

                    if current_count > max_count:
                        max_count = current_count
                        modes = [current.val]
                    elif current_count == max_count:
                        modes.append(current.val)

                    prev_val = current.val
                    current = current.right
        return modes





