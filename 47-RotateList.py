# Rotate List 
# Given the head of a linked list, rotate the list to the right by k places.

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
k = 4

if head == None or head.next == None or k == 0:
    temp = head
    while head != None:
        print(head.val, end="")
        head = head.next
    print()

else:   
    l = 1
    last = head 

    while last.next != None:
        last = last.next
        l += 1

    k = k % l
    if k == 0:
        while head != None:
            print(head.val, end="")
            head = head.next
        print()
    else:
        curr = head
        for i in range(l - k - 1):
            curr = curr.next

        last.next = head 
        head = curr.next
        curr.next = None

        while head != None:
                print(head.val, end="")
                head = head.next

# Time Complexity : O(n)
# Space Complexity : o(1)