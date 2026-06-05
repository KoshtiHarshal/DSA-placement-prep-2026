# Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

head = a

prev = None
nxt = None
curr = head

while curr != None:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
    
while prev != None:
    print(prev.val)
    prev = prev.next
    
# Time Complexity : O(n)
# Space Complexity : O(1)