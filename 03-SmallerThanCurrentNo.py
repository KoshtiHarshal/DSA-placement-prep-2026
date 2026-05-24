# How Many Numbers Are Smaller Than the Current Number
# Given the array List1, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

List1 = list(map(int, input("Enter elements: ").split(',')))
List2 = []

for i in List1:
    count = 0
    for j in List1:
        if j < i:
            count += 1
    List2.append(count)

print("Count of smaller numbers:", List2)