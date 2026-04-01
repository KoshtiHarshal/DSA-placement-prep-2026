# Reverse a given string (word).


word1 = str(input("Enter a string to reverse: "))
# Method 1: Using string slicing to reverse the string.
reversed_word = word1[::-1]
print("Reversed string:", reversed_word)

# Method 2: Using .reverse() method to reverse the string.
word12 = list(word1)
word12.reverse()
reversed_word = ''.join(word12)
print("Reversed string:", reversed_word)

# Method 3: Using a loop to iterate through the string in reverse order and construct the reversed string.
reversed_word = ""
for i in range(len(word1) - 1, -1, -1):
    reversed_word += word1[i]
print("Reversed string:", reversed_word)

#Method 4: swiping characters from the start and end of the string until they meet in the middle.
word3 = list(word1)
left = 0
right = len(word3) - 1
while left < right:
    temp = word3[left]
    word3[left] = word3[right]
    word3[right] = temp
    left += 1
    right -= 1
    
reversed_word = ''.join(word3)
print("Reversed string:", reversed_word)
    
