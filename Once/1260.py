import sys
sys.setrecursionlimit(10**6)

N, M, V = map(int, sys.stdin.readline().split())

li = [[] for i in range(N+1)]
chk = [0 for i in range(N+1)]

for i in range(M):
    X, Y = map(int,sys.stdin.readline().split())
    li[X].append(Y)
    li[Y].append(X)

for i in range(len(li)):
    li[i].sort()

def BFS(v):
    if chk[v] == 1:
        return
    chk[v] = 1
    for i in li[v]:
        if i not in bfs:
            bfs.append(i)
    for i in bfs:
        BFS(i)

def DFS(v):
    if chk[v] == 1:
        return
    result.append(v)
    chk[v] = 1
    for i in li[v]:
        DFS(i)

bfs = [V]
result = []
DFS(V)
print(*result)
chk = [0 for i in range(N+1)]
BFS(V)
print(*bfs)