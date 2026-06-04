# Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

head = a

# Approach 1: Two Passes

n = 2
l = 0 
curr = head
while curr != None:
    l += 1
    curr = curr.next
if n == l:
    head = head.next
else:
    curr = head
    for i in range(l-n-1):
        curr = curr.next
    curr.next = curr.next.next

while head != None:
    print(head.val, end=" ")
    head = head.next

# Time Complexity: O(L) where L is the length of the linked list
# Space Complexity: O(1)

# Approach 2: One Pass
m = 3
p1 = head
p2 = head

for i in range(m):
    p2 = p2.next
    
if p2 == None:
    head = head.next
    
else:
    while p2.next != None:
        p1 = p1.next 
        p2 = p2.next
    p1.next = p1.next.next

while head != None:
    print(head.val, end=" ")
    head = head.next

# Time Complexity: O(L) where L is the length of the linked list
# Space Complexity: O(1)