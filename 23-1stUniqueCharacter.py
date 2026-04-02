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