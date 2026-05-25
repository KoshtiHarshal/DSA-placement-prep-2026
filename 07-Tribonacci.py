# N-th Tribonacci Number
# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, print the value of Tn.

def tribonacci(n):
        if n == 0: 
            return 0
        if n == 1 or n == 2: 
            return 1
            
        t0, t1, t2 = 0, 1, 1
            
        for _ in range(3, n + 1):
            next_val = t0 + t1 + t2
            t0, t1, t2 = t1, t2, next_val
                
        return t2
n = int(input("Enter the number of terms: "))
print(tribonacci(n))

# Time Complexity: O(n) where n is the input number, because we are iterating through the loop n-2 times to calculate the Tribonacci number.
# Space Complexity: O(1) because we are using a constant amount of space to store the last three Tribonacci numbers.