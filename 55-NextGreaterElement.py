# Next Greater Element I
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Print an array ans of length nums1.length such that ans[i] is the next greater element as described above.

nums1 = [4,1,2]
nums2 = [1,3,4,2]

n = len(nums2)

ans = {}
st = []

for i in range(n-1,-1,-1):
    while len(st)>0 and st[-1]<=nums2[i]:
        st.pop()
    if len(st) == 0:
        ans[nums2[i]] = -1
    else:
        ans[nums2[i]] = st[-1]

    st.append(nums2[i])
        
res = []
for i in nums1:
    res.append(ans[i])

print(res)