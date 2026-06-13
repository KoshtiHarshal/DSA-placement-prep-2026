# Linked List Cycle II
# Given the head of a linked list, print the node where the cycle begins. If there is no cycle, print null.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
# Do not modify the linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)

a.next = b
b.next = c
c.next = d
d.next = b

head = a

slow = head
fast = head
        
isCycle = False

while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        isCycle = True
        break
         
if not isCycle:
    print("None")

l = 0
while slow.next != fast:
    slow = slow.next
    l += 1
        
l += 1
slow = slow.next

slow = head
fast = head

for i in range(l):
    fast = fast.next
        
while slow != fast:
    slow = slow.next
    fast = fast.next

print(slow.val)

# Time Complexity : O(N)
# Space Complexity : O(1)