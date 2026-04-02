# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

Num = [2, 7, 6, 5, 3, 11, 4, 10]
Target = 9

n=len(Num)
dist1 = {}

for i in range(n):
    rem = Target - Num[i]
    if rem in dist1:
        print([dist1[rem], i])
        dist1[Num[i]] = i
    else:
        dist1[Num[i]] = i
        