import sys

N = int(input())
li = []
cost = [0]*(N)
for i in range(N):
    li.append(int(sys.stdin.readline()))
try:
    cost[0] = li[0]
    cost[1] = max(li[0]+li[1],li[1]) 
    cost[2] = max(li[0]+li[2],li[1]+li[2])
    for i in range(3,len(li)):
        cost[i] = max(li[i-1]+li[i] + cost[i-3], cost[i-2] + li[i])
    print(cost.pop())
except:
    print(cost.pop())