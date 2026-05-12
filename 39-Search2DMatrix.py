# Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, print true if target is in matrix or false otherwise.

# Example 1:   
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 35

row = len(matrix)
cols = len(matrix[0])

l = 0
r = row * cols - 1

while l <= r:
    mid = (l + r) // 2
    
    if matrix[mid // cols][mid % cols] == target:
        print("true")
        break
    elif matrix[mid // cols][mid % cols] < target:
        l = mid + 1
    else:
        r = mid - 1
else:    
    print("false")

# Time Complexity: O(log(m*n)) where m is the number of rows and n is the number of columns in the matrix.
# Space Complexity: O(1) since we are using only a constant amount of extra space.