# Remove Duplicates from a Sorted List
# Given a sorted linked list, remove all duplicates such that each element appears only once. Return the linked list sorted as well.
list1 = list(map(int, input("Enter the elements of the list: ").split(',')))
n = len(list1)

start1 = 0
for i in range(1, n):
    if list1[i] != list1[start1]:
        start1 += 1
        list1[start1] = list1[i]
        
print("The list after removing duplicates is:", list1[0:start1+1])


# Time Complexity: O(n)
# Space Complexity: O(1)


#Given a sorted linked list, remove all duplicates such that each element appears twice. Return the linked list sorted as well.

start2 = 1
for i in range(2, n):
    if list1[i] != list1[start2-1]:
        start2 += 1
        list1[start2-1] = list1[i]

print("The list after removing duplicates is:", list1[0:start2+1])

# Time Complexity: O(n)
# Space Complexity: O(1)