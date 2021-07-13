import sys
N, K = map(int,input().split())
li = [[0,0]]
cost = [[0 for i in range(K+2)] for i in range(N+2)] 
for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))

for i in range(1,N+1):
    for j in range(1,K+1):
        if li[i][0] <= j:
            cost[i][j] = max(li[i][1] + cost[i-1][j-li[i][0]],cost[i-1][j])
        else:
            cost[i][j] = cost[i-1][j]
print(cost[N][K])