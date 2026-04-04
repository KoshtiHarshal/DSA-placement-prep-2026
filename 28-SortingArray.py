# Sort an Array
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Arr1 = list(map(int, input("Enter the array: ").split(",")))
# Arr1 = [2,1,5,3,7,6,4]
n = len(Arr1)

# Bubble Sort

for i in range(n):
    isSwap = False
    for j in range(n-i-1):
        if Arr1[j]>Arr1[j+1]:
            Arr1[j], Arr1[j+1] = Arr1[j+1], Arr1[j]
            isSwap = True
            
    if not isSwap:
        break    
print("Sorted array by Bubble sort: ", Arr1)
#Space Complexity : O(1)
#Time Complexity : O(n²),Ω(n)


# Insertion sort

for i in range(1,n):
    key = Arr1[i]
    j = i-1
    while j>=0 and Arr1[j]>key:
        Arr1[j+1]=Arr1[j]
        j-=1
        Arr1[j+1] = key
        
print("Sorted array by Insertion sort: ", Arr1)
#Space Complexity : O(1)
#Time Complexity : O(n²),Ω(n)


# Selection Sort

for i in range(n):
    mn = Arr1[i]
    index = i
    for j in range(i+1,n):
        if Arr1[j]<mn:
            mn = Arr1[j]
            index = j
    Arr1[i],Arr1[index] = Arr1[index],Arr1[i]
print("Sorted array by Selection sort: ", Arr1)       
#Space Complexity : O(1)
#Time Complexity : O(n²),Ω(n²)

