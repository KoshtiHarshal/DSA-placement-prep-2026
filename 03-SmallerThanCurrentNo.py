List1 = list(map(int, input("Enter elements: ").split(',')))
List2 = []

for i in List1:
    count = 0
    for j in List1:
        if j < i:
            count += 1
    List2.append(count)

print("Count of smaller numbers:", List2)