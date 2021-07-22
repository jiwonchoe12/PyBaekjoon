import sys
N = int(input())

li = [[-2] for i in range(N+1)]

for i in range(1,N+1):
    ll = list(map(int, sys.stdin.readline().split()))
    for k in ll:
        li[i].append(k)

cnt = [0,0,0]

def solve(n,m,x):
    tmp = li[n][m]
    for i in range(n,n+x):
        for j in range(m,m+x):
            if li[i][j] != tmp:
                inter = x//3
                solve(n,m,inter)
                solve(n+inter,m,inter)
                solve(n,m+inter,inter)
                solve(n+inter,m+inter,inter)
                solve(n+inter+inter,m,inter)
                solve(n,m+inter+inter,inter)
                solve(n+inter+inter,m+inter+inter,inter)
                solve(n+inter+inter,m+inter,inter)
                solve(n+inter,m+inter+inter,inter)
                return
    if tmp == 1:
        cnt[2] += 1
    elif tmp == 0:
        cnt[1] += 1
    elif tmp == -1:
        cnt[0] += 1
    return 

solve(1,1,N)
print(*cnt,sep='\n')