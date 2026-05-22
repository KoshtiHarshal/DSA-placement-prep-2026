# Sqrt(x)
# Given a non-negative integer x, print the square root of x rounded down to the nearest integer. The printed integer should be non-negative as well.

# Example 1:
# Input: x = 4
# Output: 2

# Example 2:
# Input: x = 8
# Output: 2

x=100

if x==0 or x==1:
    print("The square root of x is:", x)

l = 1
r = x
ans = 0

while l <= r:
    mid = (l + r) // 2
    midSquare = mid * mid
    
    if midSquare == x:
        ans = mid
        break
    elif midSquare < x:
        l = mid + 1
        ans = mid
    else:
        r = mid - 1
        
print("The square root of x is:", ans)

# Time Complexity: O(log x)
# Space Complexity: O(1)