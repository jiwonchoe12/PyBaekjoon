import sys
N = int(input())

li = []
chk = [[0 for i in range(N)] for i in range(N)]
cnt = 0
result = []
for i in range(N):
    li.append(list(map(int,sys.stdin.readline().strip())))

def DFS(i,j):
    global cnt
    if i < 0 or j < 0 or i >= N or j >= N:
        return
    if chk[i][j] == 1:
        return
    if li[i][j] == 0:
        return
    chk[i][j] = 1
    cnt += 1
    DFS(i+1,j)
    DFS(i-1,j)
    DFS(i,j+1)
    DFS(i,j-1)

for i in range(N):
    for j in range(N):
        DFS(i,j)
        if cnt != 0:
            result.append(cnt)
        cnt = 0
result.sort()
print(len(result))
print(*result,sep='\n')