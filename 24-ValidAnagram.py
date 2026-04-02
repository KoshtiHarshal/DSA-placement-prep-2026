# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# a = "Listen"
# b = "silent"

a = "car"
b = "rat"

a = a.lower()
b = b.lower()

# Method 1: Sorting
if sorted(a) == sorted(b):
    print(True)
else:
    print(False)

# Method 2: Frequency Count

if len(a) != len(b):
    print(False)

freq = {}
for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
        
for i in b:
    if i in freq:
        freq[i] -= 1
    else:
        print(False)
        break

for i in freq.values():
    if i != 0:
        print(False)
        break
    else:
        print(True)