import sys

N = int(input())
M = int(input())

li = [[] for i in range(N+1)]
chk = [0 for i in range(N+1)]
cnt = 0
for i in range(M):
    X,Y = map(int,sys.stdin.readline().split())
    li[X].append(Y)
    li[Y].append(X)

def DFS(v):
    global cnt
    if chk[v] == 1:
        return
    chk[v] = 1
    cnt += 1
    for i in li[v]:
        DFS(i)
DFS(1)
print(cnt-1)