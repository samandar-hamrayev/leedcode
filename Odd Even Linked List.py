from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even_head = head.next
        even = even_head
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        odd.next = even_head
        return head


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

head = create_linked_list([1, 2, 3, 4, 5])
sol = Solution()
new_head = sol.oddEvenList(head)
print_linked_list(new_head)

