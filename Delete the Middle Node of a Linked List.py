from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        dummy = ListNode(0, head)
        fast = head
        slow = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return dummy.next


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head: Optional[ListNode]):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

head = create_linked_list([1, 3, 4, 7, 1, 2, 6])
sol = Solution()
new_head = sol.deleteMiddle(head)
print_linked_list(new_head)
