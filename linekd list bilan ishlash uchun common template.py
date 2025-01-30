class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head







# Node-larni yaratamiz
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node4 = ListNode(1)
node5 = ListNode(1)

# Node-larni bog'laymiz
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# `head` node
head = node1

# `Solution` obyektini yaratamiz va `removeNodes` ni chaqiramiz
solution = Solution()
new_head = solution.deleteDuplicates(head)

# Linked listni chop etish funksiyasi
def printList(head: ListNode):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Natijani chop etamiz
printList(new_head)





