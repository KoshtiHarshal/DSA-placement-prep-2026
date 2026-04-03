# A Substring is a contiguous sequence of characters within a string.
# Given a string s, return the number of substrings in s that have all distinct characters.
s = "xyzzaz"
# s = "aababcabc"

n = len(s)
count = 0

for i in range(n-2):
    if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
        count += 1
                
print(count)