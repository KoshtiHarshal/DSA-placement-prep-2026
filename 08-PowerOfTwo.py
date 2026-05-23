def isPowerOfTwo(n: int) -> bool:
    # Any number less than or equal to 0 cannot be a power of two
    if n <= 0:
        return False
        
    # Keep dividing by 2 as long as the number is even
    while n % 2 == 0:
        n = n // 2
        
    # If we successfully reached 1, it was a power of two
    return n == 1

print(isPowerOfTwo(1))    # True
print(isPowerOfTwo(2))    # True
print(isPowerOfTwo(10))   # False