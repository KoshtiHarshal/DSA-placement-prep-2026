# Runner Sum
# Given an array of integers, return a new array where each element at index i is the sum of the elements from index 0 to i in the original array.
arr1 = list(map(int, input("Enter the elements of the first array: ").split(',')))
n=len(arr1)
runner_sum = [arr1[0]]
for i in range(1, n):
    runner_sum.append(runner_sum[i-1] + arr1[i])
print("The runner sum of the array is:", runner_sum)
