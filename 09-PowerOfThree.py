# Power of Three
# Given an integer n, return true if it is a power of three. Otherwise, return false.

def isPowerOfThree(n: int) -> bool:
    # Any number less than or equal to 0 cannot be a power of three
    if n <= 0:
        return False
        
    # Keep dividing by 3 as long as the number is divisible by 3
    while n % 3 == 0:
        n = n // 3
        
    # If we successfully reached 1, it was a power of three
    return n == 1

print(isPowerOfThree(27))  # True
print(isPowerOfThree(81))  # True
print(isPowerOfThree(10))  # False