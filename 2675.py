import sys
N = int(input())
for i in range(N):
    arr = list(map(str,sys.stdin.readline().split()))
    for k in arr[1]:
        for j in range(int(arr[0])):
            print(k, end='')
    print()