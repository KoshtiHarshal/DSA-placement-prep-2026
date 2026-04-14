# Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0,1, and 2 to represent the color red, white, and blue, respectively.


# Method-1: Using Counting Sort
nums1 = [2,0,2,1,0,0,1,1,2,1]

n = len(nums1)
mx = max(nums1)

freq = [0]*(mx+1)

for i in nums1:
    freq[i]+=1
    
nums1=[]

for i in range(0,mx+1):
    while freq[i]>0:
        nums1.append(i)
        freq[i]-=1
        
print("The Sorted color according to red, white and blue is :", nums1)


# Method-2 : 2 pointer approach

nums2 = [2,0,2,1,0,0,1,1,2,1]
left = 0 
right = len(nums2)-1
i = 0

while i<=right:
    if nums2[i] == 1:
        i+=1
    elif nums2[i] == 0:
        nums2[i],nums2[left] = nums2[left],nums2[i]
        i+=1
        left += 1
    else:
        nums2[i],nums2[right] = nums2[right],nums2[i]
        right -= 1

print("The Sorted color according to red, white and blue is :", nums2)