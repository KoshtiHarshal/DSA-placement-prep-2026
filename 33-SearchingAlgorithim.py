# Searching Algorithm
# Given an array of integer nums and an integer target, write a program to search target in nums. If target exists, then print its index. Otherwise print, Not in the array.

nums = [1,2,3,4,5,6,7,8,9]
n = len(nums)
target = 7

# linear search
for i in range(n):
    if nums[i] == target:
        print(i)
        
#Space Complexity : O(1)
#Time Complexity : O(nlogn)
             
#Binary search 
l = 0
r = n - 1

while l<=r:
    mid = (l+r)//2
    if target == nums[mid]:
        print(mid)
        break
    elif target > nums[mid]:
        l = mid+1
    else:
        r = mid-1
        
#Space Complexity : O(n)
#Time Complexity : O(nlogn)