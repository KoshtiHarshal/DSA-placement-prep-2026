# Remove Duplicates from Sorted List
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
a = ListNode(2)
b = ListNode(2)
c = ListNode(2)
d = ListNode(3)
e = ListNode(4)
f = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

head = a

if head == None or head.next == None:
    print(head)

curr = head
while curr != None and curr.next != None:
    if curr.next.val == curr.val:
        curr.next = curr.next.next
    else:
        curr = curr.next

while head != None:
    print(head.val)
    head = head.next
    
# Time Complexity: O(n)
# Space Complexity: O(1)