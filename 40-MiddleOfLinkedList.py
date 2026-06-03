# Middle of Linked List
# Given the head of a singly linked list, print the middle node of the linked list.
# If there are two middle nodes, print the second middle node.

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)
# a.next = b
# b.next = c
# c.next = d
# d.next = e

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

head = a

# Approach 1: Two Passes
curr = head
l = 0 

while curr != None:
    curr = curr.next
    l += 1
    
curr = head 
for i in range(l//2):
    curr = curr.next
    
while curr != None:
    print(curr.val, end=" ")
    curr = curr.next

    
# Time Complexity: O(n)
# Space Complexity: O(1) 

print()

# Approach 2: One Pass
slow = head
fast = head

while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

while slow != None:
    print(slow.val, end=" ")
    slow = slow.next
    
# Time Complexity: O(n)
# Space Complexity: O(1)