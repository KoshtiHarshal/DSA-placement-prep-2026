# Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Print true if there is a cycle in the linked list. Otherwise, Print false.

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
result = False

while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        result = True
        break

print(result)

# Time Complexity : O(N)
# Space Complexity : O(1)