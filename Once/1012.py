import sys
sys.setrecursionlimit(10**6)
T = int(input())
cnt = 0
def DFS(i,j, m, n, chk, li):
    global cnt
    if i < 0 or j < 0 or i >= n or j >= m:
        return
    if chk[i][j] == 1 or li[i][j] == 0:
        return
    chk[i][j] = 1
    cnt += 1
    DFS(i+1,j, m, n, chk, li)
    DFS(i-1,j, m, n, chk, li)
    DFS(i,j+1, m, n, chk, li)
    DFS(i,j-1, m, n, chk, li)



for i in range(T):
    M,N,K = map(int,sys.stdin.readline().split())
    li = [[0 for i in range(M)] for i in range(N)]
    chk = [[0 for i in range(M)] for i in range(N)]
    result = 0
    for j in range(K):

        X, Y = map(int,sys.stdin.readline().split())
        li[Y][X] = 1
    
    for y in range(N):
        for x in range(M):
            DFS(y,x,M,N,chk, li)
            if cnt != 0:
                result += 1
            cnt = 0
    print(result)
