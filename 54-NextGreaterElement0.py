# Next Greater Elment


nums = [3,1,7,4,9,6,8]

n = len(nums)

ans = [0]*n
st = []

for i in range(n-1,-1,-1):
    while len(st)>0 and st[-1]<=nums[i]:
        st.pop()
    if len(st) == 0:
        ans[i] = -1
    else:
        ans[i] = st[-1]

    st.append(nums[i])
    
print (ans)

# Time Complexity = O(N)
# Space Complexity = O(N)