import sys
from collections import deque
N, M = map(int,input().split())

li = []
que = deque()
que.append([0,0,0])
for i in range(N):
    li.append(list(map(int,sys.stdin.readline().strip())))
cost = [[[99999]*M for i in range(N)],[[99999]*M for i in range(N)]]
cost[0][0][0] = 1
def BFS():
    while que:
        for i in range(len(que)):
            xy = que.popleft()
            i = xy[0]
            j = xy[1]
            b = xy[2]
            if b == 0 and i+1 < N and li[i+1][j] == 1 and cost[b+1][i+1][j] > cost[b][i][j] + 1:
                cost[b+1][i+1][j] = cost[b][i][j] + 1
                que.append([i+1,j,1])
            if b == 0 and i-1 >= 0 and li[i-1][j] == 1 and cost[b+1][i-1][j] > cost[b][i][j] + 1:
                cost[b+1][i-1][j] = cost[b][i][j] + 1
                que.append([i-1,j,1])
            if b == 0 and j-1 >= 0 and li[i][j-1] == 1 and cost[b+1][i][j-1] > cost[b][i][j] + 1:
                cost[b+1][i][j-1] = cost[b][i][j] + 1
                que.append([i,j-1,1])
            if b == 0 and j+1 < M and li[i][j+1] == 1 and cost[b+1][i][j+1] > cost[b][i][j] + 1:
                cost[b+1][i][j+1] = cost[b][i][j] + 1
                que.append([i,j+1,1])
            
            if i+1 < N and li[i+1][j] == 0 and cost[b][i+1][j] >= cost[b][i][j] + 1:
                cost[b][i+1][j] = cost[b][i][j] + 1
                que.append([i+1,j,b])
            if i-1 >= 0 and li[i-1][j] == 0 and cost[b][i-1][j] >= cost[b][i][j] + 1:
                cost[b][i-1][j] = cost[b][i][j] + 1
                que.append([i-1,j,b])
            if j-1 >= 0 and li[i][j-1] == 0 and cost[b][i][j-1] >= cost[b][i][j] + 1:
                cost[b][i][j-1] = cost[b][i][j] + 1
                que.append([i,j-1,b])
            if j+1 < M and li[i][j+1] == 0 and cost[b][i][j+1] >= cost[b][i][j] + 1:
                cost[b][i][j+1] = cost[b][i][j] + 1
                que.append([i,j+1,b])
BFS()
if cost[-1][-1][-1] == 99999 and cost[0][-1][-1] == 99999:
    print(-1)
else:
    print(min(cost[-1][-1][-1], cost[0][-1][-1]))
