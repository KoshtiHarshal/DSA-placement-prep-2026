#Subtract the product and sum of the digits of an integer.

n = int(input("Enter a number: "))

sum = 0
product = 1
for i in str(n):
    sum += int(i)
    product *= int(i)
print (product - sum)

# Time Complexity: O(log n) where n is the input number, because we are iterating through each digit of the number.
# Space Complexity: O(1) because we are using a constant amount of space to store the sum and product of the digits.