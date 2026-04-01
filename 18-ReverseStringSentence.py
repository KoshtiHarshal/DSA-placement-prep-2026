# Reverse a given string (sentence) while keeping the order of words intact.

# Method 1: Using string methods to split the sentence into words, reverse the list of words, and join them back into a sentence.
sentence1 = str(input("Enter a sentence to reverse: "))
words = sentence1.split()
words.reverse()
reversed_sentence = ' '.join(words)
print("Reversed sentence:", reversed_sentence)  

# Method 2: Using a loop to iterate through the sentence in reverse order and construct the reversed sentence.
sentence2 = str(input("Enter a sentence to reverse: "))
reversed_sentence = ""
for i in range(len(sentence2) - 1, -1, -1):
    reversed_sentence += sentence2[i]
print("Reversed sentence:", reversed_sentence)

