import sys

N = int(input())
A = list(map(int,sys.stdin.readline().split()))
M = int(input())
B = list(map(int,sys.stdin.readline().split()))
ll = set(B)
d = {}

for i in A:
    if i in ll:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

for i in B:
    if i in d:
        print(d[i],end=' ')
    else:
        print(0, end=' ')