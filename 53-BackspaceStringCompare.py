# Backspace String Compare
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

s = "ab#c" 
t = "ad#d"

s1 = []
t1 = []

for ch in list(s):
    if ch != "#":
        s1.append(ch)
    elif len(s1)>0:
        s1.pop()

for ch in list(t):
    if ch != "#":
        t1.append(ch)
    elif len(t1)>0:
        t1.pop()

if s1 == t1:
    print("True")
else:
    print("False")

# Time Complexity = O(N)
# Space Complexity = O(1)