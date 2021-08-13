import sys
N, M = map(int, sys.stdin.readline().split())

li = []
que = [[0,0]]
for i in range(N):
    li.append(list(sys.stdin.readline().strip()))
chk = [[0] * M for i in range(N)]

def BFS():
    global li, chk
    cnt = 0
    while que:
        cnt += 1
        for _ in range(len(que)):
            xy = que.pop(0)
            i = xy[0] 
            j = xy[1]
            if i == N-1 and j== M-1:
                return cnt
            chk[i][j] = 1
            if i+1 < N and li[i+1][j] == '1' and not chk[i+1][j]:
                chk[i+1][j] = 1
                que.append([i+1,j])
            if i-1 >= 0 and li[i-1][j] == '1' and not chk[i-1][j]:
                chk[i-1][j] = 1
                que.append([i-1,j])
            if j+1 < M and li[i][j+1] == '1' and not chk[i][j+1]:
                chk[i][j+1] = 1
                que.append([i,j+1])
            if j-1 >= 0 and li[i][j-1] == '1' and not chk[i][j-1]:
                chk[i][j-1] = 1
                que.append([i,j-1])

print(BFS())