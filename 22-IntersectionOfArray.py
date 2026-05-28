# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

num1 = [1, 2, 2, 1]
num2 = [2, 2]

set1 = set(num1)
set2 = set(num2)

result = set1.intersection(set2)
print(list(result))

# Time Complexity: O(n + m) where n and m are the lengths of nums1 and nums2 respectively.
# Space Complexity: O(min(n, m)) where n and m are the lengths of nums1 and nums2 respectively, since we are storing the unique elements of the smaller array in a set.