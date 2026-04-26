# Given a sorted array of distinct integers and a target value, print the index if the target is found. If not, print the index where it would be if it were inserted in order.


nums = [2,4,6,7,9]
target = 5
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
        
print("This is lower bound answer :", ans1)


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
        
print("This is upper bound answer :", ans2)

#Time Complexity : O(nlogn)