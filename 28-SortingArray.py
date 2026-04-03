# Sort an Array
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Arr1 = list(map(int, input("Enter the array: ").split(",")))

# Bubble Sort
n = len(Arr1)

for i in range(n):
    isSwap = False
    for j in range(n-i-1):
        if Arr1[j]>Arr1[j+1]:
            Arr1[j], Arr1[j+1] = Arr1[j+1], Arr1[j]
            isSwap = True
            
    if not isSwap:
        break    
print("Sorted array: ", Arr1)
#Space Complexity : O(1)
#Time Complexity : O(n²),Ω(n)



