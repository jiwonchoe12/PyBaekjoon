import sys
n = input()
arr = list(map(int, sys.stdin.readline().split()))
m = max(arr)
for i in range(len(arr)):
    arr[i] = arr[i]/m * 100
print(sum(arr) / len(arr))