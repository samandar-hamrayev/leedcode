# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            prev, curr = kth.next, prev_group.next
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev, curr = curr, next_node

            temp = prev_group.next
            prev_group.next = prev
            prev_group = temp

def create_linked_list(nums: list[int]):
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for i in range(1, len(nums)):
        current.next = ListNode(nums[i])
        current = current.next
    return head

head = create_linked_list([1, 2, 3, 4, 5])

sol = Solution()
print(sol.reverseKGroup(head, 2).val)
