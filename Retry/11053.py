import sys
N = int(input())
li = list(map(int, sys.stdin.readline().split()))
length = [0] * N
for i in range(N):
    length[i] = 1
    for j in range(0,i):
        if li[j] < li[i]:
            length[i] = max(length[j]+1, length[i])
print(length)
