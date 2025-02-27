# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def split(node: ListNode):
            fast = node.next
            slow = node

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            second = slow.next
            slow.next = None
            return second

        def merge(left, right):
            dummy = ListNode()
            tail = dummy
            while left and right:
                if left.val < right.val:
                    tail.next, left = left, left.next
                else:
                    tail.next, right = right, right.next
                tail = tail.next
            tail.next = left if left else right
            return dummy.next


        def merge_sort(head):
            if not head or not head.next:
                return head
            second = split(head)

            head = merge_sort(head)
            second = merge_sort(second)

            return merge(head, second)
        return merge_sort(head)


head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

sol = Solution()
res = sol.sortList(head)

def print_list(head):
    res =  []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

print_list(res)




