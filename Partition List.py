# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallers = ListNode(0)
        small_head = smallers
        greaters = ListNode(0)
        great_head = greaters

        while head:
            if head.val >= x:
                greaters.next = head
                greaters = greaters.next
            else:
                smallers.next = head
                smallers = smallers.next
            head = head.next
        greaters.next = None
        smallers.next = great_head.next
        return small_head.next


def create_linked_list(nums: list[int]) -> ListNode:
    head = ListNode(0)
    curr = head
    i = 0
    while i < len(nums):
        curr.next = ListNode(nums[i])
        curr = curr.next
        i += 1
    return head.next

def print_linked_list(head: ListNode) -> None:
    result = []
    while head:
        result.append(str(head.val))
        head = head.next

    print(" -> ".join(result))

head = create_linked_list([1,4,3,2,5,2])
sol = Solution()
res = sol.partition(head, 3)
print_linked_list(res)


