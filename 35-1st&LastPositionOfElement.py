# Given an array of integer (nums) sorted in non-decreasing order, find the starting and ending position of a given target value.

# if target is not found in the array, print [-1, -1]

nums = [5,7,7,8,8,10]
target = 7
n = len(nums)


# Lower Bound
l1 = 0
r1 = n-1
ans1 = n

while l1<=r1:
    mid1 = (l1+r1)//2
     
    if nums[mid1] >= target:
        ans1 = mid1
        r1 = mid1 - 1
    else:
        l1 = mid1 + 1

# Upper Bound
l2 = 0
r2 = n-1
ans2 = n

while l2<=r2:
    mid2 = (l2+r2)//2
     
    if nums[mid2] > target:
        ans2 = mid2
        r2 = mid2 - 1
    else:
        l2 = mid2 + 1
        
lb = ans1
ub = ans2

if lb == ub:
    print([-1,-1])
else:
    print([lb,ub-1])
    
#Time Complexity : O(nlogn)