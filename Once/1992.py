import sys
N = int(input())

li = [[-1] for i in range(N+1)]

for i in range(1,N+1):
    ll = list(map(int, sys.stdin.readline().strip()))

    for k in ll:
        li[i].append(k)

result = []

def solve(n,m,x):
    zflag = 1
    oflag = 1
    for i in range(n,n+x):
        for j in range(m,m+x):
            if li[i][j] == 0:
                oflag = 0
            elif li[i][j] == 1:
                zflag = 0
    if oflag == 0 and zflag == 0:
        tmp = x//2
        result.append('(')
        solve(n,m,tmp)
        solve(n,m+tmp,tmp)
        solve(n+tmp,m,tmp)
        solve(n+tmp,m+tmp,tmp)
        result.append(')')
        return
    if zflag == 1:
        result.append(0)
    else:
        result.append(1)
    return
    
solve(1,1,N)
print(*result,sep='')