from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        left, mid, right = self.divide_linked_list(head)

        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)

        return root

    def divide_linked_list(self, head: ListNode):
        if not head:
            return None, None, None
        if not head.next:
            return None, head, None

        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        mid = slow
        right = mid.next
        mid.next = None

        if prev:
            prev.next = None

        return head if prev else None, mid, right


head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)
# head.next.next.next.next.next = ListNode(11)
# head.next.next.next.next.next.next = ListNode(13)

sol = Solution()
first, mid, second = sol.divide_linked_list(head)
print(mid.val)

print(sol.sortedListToBST(head).val)





