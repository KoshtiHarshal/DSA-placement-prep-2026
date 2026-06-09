# Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)
a1.next = a2
a2.next = a3

b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

l1 = a1
l2 = b1

curr1 = l1
curr2 = l2
ans = ListNode(-1)
c = 0
curr3 = ans

while curr1 != None or curr2 != None:
    total = c 

    if curr1 != None:
        total += curr1.val
        curr1 = curr1.next
    if curr2 != None:
        total += curr2.val
        curr2 = curr2.next

    # if total>9:
    #     c = 1
    #     total -= 10
    c, total = divmod(total, 10)

    newNode = ListNode(total)
    curr3.next = newNode
    curr3 = curr3.next

if c>0:
    newNode = ListNode(c)
    curr3.next = newNode

while ans.next != None:
    print(ans.next.val, end=" ")
    ans.next = ans.next.next

# Time Complexity : O(max(N, M))
# Space Complexity : O(max(N, M))