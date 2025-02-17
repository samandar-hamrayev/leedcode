class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def in_order(root: TreeNode) -> list[int]:
    res =[]
    curr = root
    while curr is not None:
        if curr.left is None:
            res.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right is not None and prev.right != curr:
                prev = prev.right

            if prev.right is None:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                res.append(curr.val)
                curr = curr.right
    return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(in_order(root))
