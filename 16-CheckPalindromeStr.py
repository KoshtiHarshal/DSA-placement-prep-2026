#Check if a given word is a palindrome or not.


Word = str(input("Try to enter a palindrome word: "))
# Method 1: Using string slicing to reverse the word and compare it with the original word.
if Word == Word[::-1]:
    print(Word, "is a palindrome.")
else:
    print(Word, "is not a palindrome.")

# Method 2: Using a loop to compare characters from the start and end of the word.
is_palindrome = True
for i in range(len(Word) // 2):
    if Word[i] != Word[-(i + 1)]:
        is_palindrome = False
        break
if is_palindrome:
    print(Word, "is a palindrome.")
else:
    print(Word, "is not a palindrome.")

   

#Check if a given sentence is a palindrome or not, ignoring spaces, punctuation, and capitalization.
Sentence = str(input("Try to enter a palindrome sentence: ")) 
# Method 1: Using string methods to remove spaces and punctuation, and convert to lowercase before checking for palindrome.
Sentence1 = Sentence.lower()
Sentence1 = Sentence1.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("'", "").replace('-', "").replace(":", "")
if Sentence1 == Sentence1[::-1]:
    print(Sentence1, "is a palindrome.")
else:
    print(Sentence1, "is not a palindrome.")

#Method 2: Using regular expressions to remove non-alphanumeric characters and convert to lowercase before checking for palindrome.
def isAlphanumeric(Sentence2):
    x = ord(Sentence2)
    if (x >= 48 and x <= 57) or (x >= 65 and x <= 90) or (x >= 97 and x <= 122): 
        return True
    else:
        return False
Sentence2 = str(input("Try to enter a palindrome sentence: "))
Sentence2 = Sentence2.lower()

i = 0
j = len(Sentence2) - 1

while i < j:
    if not isAlphanumeric(Sentence2[i]):
        i += 1
    elif not isAlphanumeric(Sentence2[j]):
        j -= 1
    elif Sentence2[i] == Sentence2[j]:
        i += 1
        j -= 1
    else:
        print(Sentence2, "is not a palindrome.")
        break
else:    print(Sentence2, "is a palindrome.")    

