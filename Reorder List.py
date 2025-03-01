# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        prev = None
        while second:
            next_val = second.next
            second.next = prev
            prev = second
            second = next_val
        second = prev

        first = head
        while second:
            next_first, next_second = first.next, second.next
            first.next = second
            second.next = next_first
            first, second = next_first, next_second
