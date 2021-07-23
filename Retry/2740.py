import sys
N, M = map(int,input().split())

li = []
li2 = []
for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))

M, K = map(int,input().split())
result = [[0 for i in range(K)] for i in range(N)]
for i in range(M):
    li2.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j] += li[i][k] * li2[k][j]
    
for i in result:
    print(*i)
