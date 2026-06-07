# Intersection of Two Linked Lists
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a1 = ListNode(4)
a2 = ListNode(1)
b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(1)
c1 = ListNode(8)
c2 = ListNode(4)
c3 = ListNode(5)

a1.next = a2
a2.next = c1
a2.next = c3
b1.next = b2
b2.next = b3
b3.next = c1
c1.next = c2
c2.next = c3

headA = a1
headB = b1

p1 = headA
p2 = headB

while p1 != p2:
    p1 = p1.next if p1 != None else headB
    p2 = p2.next if p2 != None else headA

if p1:
    print(f"Intersected at node with value: {p1.val}")
else:
    print("No intersection")

# Time Complexity : O(N+M)
# Space Complexity : o(1)   