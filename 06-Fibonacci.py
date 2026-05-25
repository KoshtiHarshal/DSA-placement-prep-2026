# Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
            # F(0) = 0, F(1) = 1
            # F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n=int(input("Enter the number of terms: "))
print(fibonacci(n))

# Time Complexity: O(2^n) where n is the input number, because we are making two recursive calls for each value of n greater than 1.
# Space Complexity: O(n) because of the recursive call stack, which can go as deep as n in the worst case.