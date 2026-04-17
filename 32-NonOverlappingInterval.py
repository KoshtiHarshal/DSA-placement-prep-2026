# Given an array of intervals (itvl) where itvl[i] = [start,end], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Note that intervals which only touch at a point are non-overlapping. For example, [1,2] and [2,3] are non-overlapping.

itvl = [[1,2],[2,3],[3,4],[1,3]] 
# itvl = [[1,5],[8,9],[2,3],[6,7],[6,9]] 

itvl.sort(key = lambda x : x[1])
n = len(itvl)

prev = 0 
count = 1

for i in range(1,n):
    if itvl[i][0] >= itvl[prev][1]:
        count += 1
        prev = i

print("Number of interval need to remove is/are :",n-count)