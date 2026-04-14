# Sort an Array - Part-2 

#Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
    
        mid = len(arr) // 2  

        a = arr[:mid]
        b = arr[mid:]
        
        merge_sort(a)
        merge_sort(b)

        i = j = k = 0
        
        while k < len(arr):  
            if j == len(b):
                arr[k] = a[i] 
                i += 1
            elif i == len(a):
                arr[k] = b[j]
                j += 1
            elif a[i] < b[j]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k += 1
                
    return arr 

Arr1 = [7, 1, 5, 3, 2, 6, 4]
# Arr1 = list(map(int, input("Enter the array: ").split(",")))
print("Sorted Array using Merge Sort method :", merge_sort(Arr1))

#Space Complexity : O(n)
#Time Complexity : O(nlogn)


#Quick Sorting

def partition(arr,l,r):
    key = arr[r]
    start = l
    
    for i in range(l,r):
        if arr[i] <= key:
            arr[i], arr[start] = arr[start], arr[i]
            start+=1

    arr[start], arr[r] = arr[r], arr[start]
    return start

def quick_sort(arr,l=0,r=None):
    if r is None:
        r = len(arr) - 1

    if l < r:
        p = partition(arr, l, r)
        quick_sort(arr, l, p - 1)
        quick_sort(arr, p + 1, r)
    return arr
        

Arr1 = [7, 1, 5, 3, 2, 6, 4]
# Arr1 = list(map(int, input("Enter the array: ").split(",")))
print("Sorted Array using Quick Sort method :", quick_sort(Arr1))

#Space Complexity : O(1)
#Time Complexity : O(n²), Ω(nlogn)


# Counting Sort

Arr2 = [5,3,2,2,3,4,1,1,0,0,4]
n = len(Arr2)
mx = max(Arr2)

freq = [0]*(mx+1)

for i in Arr2:
    freq[i]+=1
    
Arr2=[]

for i in range(0,mx+1):
    while freq[i]>0:
        Arr2.append(i)
        freq[i]-=1
        
print("Sorted Array using Counting Sort method :", Arr2)

#Space Complexity : O(mx)
#Time Complexity : O(n)