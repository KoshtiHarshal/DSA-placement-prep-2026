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

Arr1 = [2, 1, 5, 3, 7, 6, 4]
print("Sorted Array:", merge_sort(Arr1))

#Space Complexity : O(n)
#Time Complexity : O(nlogn)