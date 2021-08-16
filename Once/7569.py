import sys
from collections import deque

M,N,H = map(int, sys.stdin.readline().split())

li = []
que = deque()
zcnt = 0

for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, sys.stdin.readline().split())))
    li.append(tmp)

for k in range(H):
    for i in range(N):
        for j in range(M):
            if li[k][i][j] == 1:
                que.append([k,i,j])
            if li[k][i][j] == 0:
                zcnt += 1

def BFS():
    cnt = 0
    global zcnt
    if zcnt == 0:
        return 0
    while que:
        cnt += 1
        for i in range(len(que)):
            xyz = que.popleft()
            k = xyz[0]
            i = xyz[1]
            j = xyz[2]

            if k+1 < H and li[k+1][i][j] == 0:
                li[k+1][i][j] = 1
                zcnt -= 1
                que.append([k+1,i,j])

            if k-1 >= 0 and li[k-1][i][j] == 0:
                li[k-1][i][j] = 1
                zcnt -= 1
                que.append([k-1,i,j])
            
            if i+1 < N and li[k][i+1][j] == 0:
                li[k][i+1][j] = 1
                zcnt -= 1
                que.append([k,i+1,j])
            
            if i-1 >= 0 and li[k][i-1][j] == 0:
                li[k][i-1][j] = 1
                zcnt -= 1
                que.append([k,i-1,j])
            
            if j+1 < M and li[k][i][j+1] == 0:
                li[k][i][j+1] = 1
                zcnt -= 1
                que.append([k,i,j+1])
            
            if j-1 >= 0 and li[k][i][j-1] == 0:
                li[k][i][j-1] = 1
                zcnt -= 1
                que.append([k,i,j-1])
            
            if zcnt == 0:
                return cnt
    return -1
print(BFS())