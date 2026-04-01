# Length of Last Word of a String
# Given a string Sentence consisting of words and spaces, return the length of the last word in the string. If the last word does not exist, return 0.
# A word is a maximal substring consisting of non-space characters only.
# Method 1: Using string methods to split the sentence into words and return the length of the last word.
sentence1 = str(input("Enter a sentence: "))
words = sentence1.split()
if len(words) == 0:
    print("Length of last word: 0")
else:    
    last_word_length = len(words[-1])
    print("Length of last word:", last_word_length)
    
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