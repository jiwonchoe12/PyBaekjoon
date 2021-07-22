import sys
N = int(input())
li = [[-1] for i in range(N+1)]

for i in range(1,N+1):
    ll = list(map(int,sys.stdin.readline().split()))
    for k in ll:
        li[i].append(k)

def solve(n,m,x):
    wflag = 1
    bflag = 1
    for i in range(n,n+x):
        for j in range(m,m+x):
            if li[i][j] == 1:
                wflag = 0
            elif li[i][j] == 0:
                bflag = 0
            elif li[i][j] == -1:
                wflag = 0
                bflag = 0
                return [bflag,wflag]
            if wflag == 0 and bflag == 0:
                return [bflag,wflag]
    for i in range(n,n+x):
        for j in range(m,m+x):
            li[i][j] = -1
    return [bflag,wflag]

bcnt = 0
wcnt = 0
interval = N

while interval > 0 :
    for i in range(1,N+1,interval):
        for j in range(1,N+1,interval):
            r_li = solve(i,j,interval)
            bcnt += r_li[0]
            wcnt += r_li[1]
    interval //= 2
print(wcnt)
print(bcnt)