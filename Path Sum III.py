class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        def dfs(node: TreeNode, current_sum):
            if not node:
                 return 0
            current_sum += node.val
            count = prefix_sum[current_sum - targetSum]
            print(bcolors.OKGREEN, count, current_sum, bcolors.ENDC)
            prefix_sum[current_sum] += 1

            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            print(bcolors.FAIL, count, current_sum, bcolors.ENDC)
            prefix_sum[current_sum] -= 1

            return count

        return dfs(root, 0)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(-9)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.left.right= TreeNode(2)
root.left.left.right = TreeNode(-2)
root.left.left.right.right = TreeNode(2)
root.left.right.right = TreeNode(1)

sol = Solution()
print(sol.pathSum(root, 8))



