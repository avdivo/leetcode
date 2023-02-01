class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    cast = []
    while list1:
        cast.append(list1.val)
        list1 = list1.next
    while list2:
        cast.append(list2.val)
        list2 = list2.next
    cast.sort()

    old = None
    for i in reversed(cast):
        old = ListNode(val=i, next=old)

    return old





a, a.next, a.next.next = ListNode(1), ListNode(2), ListNode(4)
b, b.next, b.next.next = ListNode(1), ListNode(3), ListNode(4)

a = mergeTwoLists(a, b)
while a:
    print(a.val, end=' ')
    a = a.next
print(a)


a = None
b = None

a = mergeTwoLists(a, b)
while a:
    print(a.val, end=' ')
    a = a.next
print(a)


a = None
b = ListNode(0)

a = mergeTwoLists(a, b)
while a:
    print(a.val, end=' ')
    a = a.next
print(a)