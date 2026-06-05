# Remove Duplicates from Sorted List II
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Print the linked list sorted as well.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(4)
f = ListNode(4)
g = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

head = a

dummy = ListNode(0)
dummy.next = head
prev = dummy
curr = head

while curr and curr.next:
    if curr.val == curr.next.val:
        while curr.next and curr.val == curr.next.val:
            curr = curr.next
        
        prev.next = curr.next
        
    else:
        prev = prev.next
        
    curr = curr.next
      
while dummy != None:
    print(dummy.val)
    dummy = dummy.next
    
# Time Complexity : O(n)
# Space Complexity : O(1)