from typing import Optional

# ListNode sinfi, bog'langan ro'yxatning bir tugunini ifodalaydi
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ListNode'larni yaratish uchun yordamchi funksiya
def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

# Bog'langan ro'yxatni chop qilish uchun yordamchi funksiya
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result))

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)  # Yangi bosh tugun yaratiladi
        dummy = res

        # n qadam oldinga surish
        for _ in range(n):
            head = head.next

        # Ikkala ko'rsatkichni birga oldinga surish
        while head:
            head = head.next
            dummy = dummy.next

        # Oxiridan n-o'rindagi tugunni olib tashlash
        dummy.next = dummy.next.next

        return res.next

    def addTwoNumbers(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while head1 is not None or head2 is not None or carry != 0:
            digit1 = head1.val if head1 is not None else 0
            digit2 = head2.val if head2 is not None else 0

            summa = digit1 + digit2 + carry
            digit = summa % 10
            carry = summa // 10

            tail.next = ListNode(digit)
            tail = tail.next

            head1 = head1.next if head1 is not None else None
            head2 = head2.next if head2 is not None else None

        result = dummyHead.next
        return result





# Bog'langan ro'yxat yaratish
# head = create_linked_list([1, 2, 3, 4, 5])
head1 = create_linked_list([2, 4, 3])
head2 = create_linked_list([5, 6, 4, 9])

# Solution obyektini yaratish
obj1 = Solution()

# removeNthFromEnd funksiyasini chaqirish
# new_head = obj1.removeNthFromEnd(head, 2)
new = obj1.addTwoNumbers(head1, head2)

# Yangi bog'langan ro'yxatni chop qilish
print_linked_list(new)