# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
s = "LoveLeetCode"
n = len(s)

freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
    
for i in range(n):
    if freq[s[i]] == 1:
        print(i)
        break
else:
    print(-1)
    
# Time Complexity: O(n) where n is the length of the string s, since we traverse the string twice (once to build the frequency dictionary and once to find the first non-repeating character).
# Space Complexity: O(1) since the frequency dictionary will at most contain 26 characters (assuming only lowercase English letters), which is a constant space.