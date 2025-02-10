# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = self.reverse(slow.next)
        slow.next = None
        first = head
        max_twin = -float('inf')
        while first and first.next:
            max_twin = max(max_twin, first.val + second.val)
            first = first.next
            second = second.next
        return max_twin
    def reverse(self, head: ListNode):
        """
        Reversing linked list
        :param head:
        :return:
        """
        prev = None
        current = head
        while current:
            next_node = current.next

            current.next = prev
            prev = current
            current = next_node
        return prev


