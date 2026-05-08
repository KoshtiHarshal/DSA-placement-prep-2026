# Peak Index in a Mountain Array
# You are given an integer array arr of length n where the values increase to a peak element and then decrease. Find and return the index of the peak element.
# Print the index of the peak element in the given array.

arr = [1,2,4,6,7,5,3,2]
n = len(arr)
l = 0
r = n-2
ans = n-1

while l<=r:
    mid = (l+r)//2
    
    if arr[mid]<arr[mid+1]:
        l = mid + 1
    else:
        r = mid - 1
        ans = mid
print("Index of the peak element:", ans)
print("Value of the peak element:", arr[ans])

#Time Complexity : O(logn)