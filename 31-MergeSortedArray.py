# You are given two integer arrays num1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in num1 and nums respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

num1=[1,2,3,0,0,0]
num2=[5,6,7]

m = 3
n = 3

i = m-1
j = n-1
k = m+n-1

while j>=0:
    if i<0 or num2[j]>num1[i]:
        num1[k]=num2[j]
        k-=1
        j-=1
    else:
        num1[k]=num1[i]
        k-=1
        i-=1  
        
print("The Merged Sorted array is :",num1)

