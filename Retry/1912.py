import sys
N = int(input())

li = list(map(int, sys.stdin.readline().split()))
cost = [-2000] * N
cost[0] = li[0]
for i in range(1,N):
    if li[i] > cost[i-1] + li[i]:
        cost[i] = li[i]
    else:
        cost[i] = li[i] + cost[i-1]

print(max(cost))
