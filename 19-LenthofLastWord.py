# Length of Last Word of a String
# Given a string Sentence consisting of words and spaces, return the length of the last word in the string. If the last word does not exist, return 0.
# A word is a maximal substring consisting of non-space characters only.

# Method 1: Using string methods to split the sentence into words and return the length of the last word.
sentence1 = str(input("Enter a sentence: "))
words = sentence1.split() # Split the sentence into words based on spaces. This will automatically handle multiple spaces and ignore leading/trailing spaces.
if len(words) == 0:
    print("Length of last word: 0")
else:    
    last_word_length = len(words[-1])
    print("Length of last word:", last_word_length)
    
# Time Complexity: O(n) where n is the length of the input string. The split method traverses the entire string to create the list of words.
# Space Complexity: O(m) where m is the number of words in the sentence due to the list created by the split method.
    
# Method 2: Using a loop to iterate through the sentence in reverse order and count the length of the last word until a space is encountered.
sentence2 = str(input("Enter a sentence: "))
sentence2 = sentence2.strip()  # Remove leading and trailing spaces
n = len(sentence2)
i = -1
while i >= -n and sentence2[i] != ' ':
    i= i-1
    
i= i+1  # Move back to the last character of the last word
i= i*-1 # Convert to positive index
 
print("Length of last word:",i)   

# Time Complexity: O(n) where n is the length of the input string. In the worst case, we may have to traverse the entire string if there are no spaces.
# Space Complexity: O(1) as we are using only a constant amount of extra space to store the index and length of the last word.