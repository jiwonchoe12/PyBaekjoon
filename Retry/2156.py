import sys

N = int(input())
li = []
cost = [0] * N
for i in range(N):
    li.append(int(sys.stdin.readline()))
try:
    cost[0] = li[0]
    cost[1] = max(li[0]+li[1], li[1])
    cost[2] = max(li[0]+li[2],li[1]+li[2])
    for i in range(3,N):
        cost[i] = max(li[i-1] + cost[i-3] + li[i], cost[i-2] + li[i],li[i]+li[i-1]+cost[i-4])
    print(max(cost))
except:
    print(max(cost))