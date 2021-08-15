import sys
from collections import deque
M, N = map(int, sys.stdin.readline().split())

li = []
que = deque()
zcnt = 0
for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))

def BFS():
    global zcnt
    cnt = 0
    while que:
        if zcnt == 0:
            return cnt
        cnt += 1
        for i in range(len(que)):
            xy = que.popleft()
            i = xy[0]
            j = xy[1]

            if i+1 < N and li[i+1][j] == 0:
                li[i+1][j] = 1
                zcnt -= 1
                que.append([i+1,j])
            if i-1 >= 0 and li[i-1][j] == 0:
                li[i-1][j] = 1
                zcnt -= 1
                que.append([i-1,j])
            if j+1 < M and li[i][j+1] == 0:
                li[i][j+1] = 1
                zcnt -= 1
                que.append([i,j+1])
            if j-1 >= 0 and li[i][j-1] == 0:
                li[i][j-1] = 1
                zcnt -= 1
                que.append([i,j-1])
            
            if zcnt == 0:
                return cnt

    return -1

for i in range(N):
    for j in range(M):
        if li[i][j] == 0:
            zcnt += 1
        elif li[i][j] == 1:
            que.append([i,j])
print(BFS())