List1 = list(map(int, input("Enter the elements of the list: ").split(",")))
n = len(List1)
start = 0
for i in range(n):
    if List1[i] % 2 == 0:
        temp = List1[i]
        List1[i] = List1[start]
        List1[start] = temp
        start += 1
        
print("The list after sorting by parity is:", List1)
