from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr =  head
        while curr:
            next_node = curr.next

            curr.next = prev

            prev = curr
            curr = next_node
        return prev


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

head = create_linked_list([1, 2, 3, 4, 5])
sol = Solution()
print(sol.reverseList(head))