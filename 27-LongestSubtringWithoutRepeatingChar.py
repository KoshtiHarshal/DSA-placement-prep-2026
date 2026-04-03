# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
n = len(s)
if n == 0:
    print(0)

max_length = 0
set1 = set({})
set1.add(s[0])

i = 0
j = 1
while j < n:
    while s[j] in set1:
        set1.remove(s[i])
        i += 1
    set1.add(s[j])
    j+=1
    max_length = max(max_length, j - i)
    
print(max_length)