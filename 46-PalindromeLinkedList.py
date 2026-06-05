# Palindrome Linked List
# Given the head of a singly linked list, Print true if it is a palindrome or false otherwise.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(2)
f = ListNode(1)

# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)
# f = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

head = a

if head == None or head.next == None:
    print("True ,it is a palindrome")
    
curr = head 
List = ListNode(curr.val)
current = List

while curr.next:
    curr = curr.next
    current.next = ListNode(curr.val)
    current = current.next
    
prev = None
nxt = None
curr = List

while curr != None:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
    
while prev and head:
    if prev.val != head.val:
        print("False ,it is not a palindrome") 
        break
    prev = prev.next
    head = head.next
    
else:
    print("True ,it is a palindrome")
    
# Time Complexity : O(n)
# Space Complexity : O(1)