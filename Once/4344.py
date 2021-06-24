import sys
n = int(input())
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    del arr[0]
    average = sum(arr) / len(arr)
    cnt = 0
    for j in arr:
        if j > average:
            cnt += 1
    print('%.3f%%' % ((cnt / len(arr)) * 100))