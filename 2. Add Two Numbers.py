from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    one = two = ''
    while l1:
        one = str(l1.val) + one
        l1 = l1.next
    while l2:
        two = str(l2.val) + two
        l2 = l2.next

    out = str(int(one) + int(two))

    old = None
    for i in out:
        old = ListNode(val=i, next=old)

    return old

a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)

a = addTwoNumbers(a, b)


while a:
    print(a.val, end='')
    a = a.next

print()

a = ListNode(0)
b = ListNode(0)

a = addTwoNumbers(a, b)

while a:
    print(a.val, end='')
    a = a.next