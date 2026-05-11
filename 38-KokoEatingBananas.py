# Koko Eating Bananas
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during that hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

piles = [30,11,23,4,20]
ans = 0
for pile in piles:
    ans = max(pile+mid-1)//mid
    print(ans)
h = 5
l = 1
r = max(piles)
k = r
while l <= r:
    mid  = (l + r) // 2
    if ans > h:
        l = mid + 1
    else:
        k = mid 
        r = mid - 1
        
print("The minimum integer k such that Koko can eat all the bananas within h hours is:", k)

# Time Complexity: O(n log m) where n is the number of piles and m is the maximum number of bananas in a pile.
# Space Complexity: O(1)    