import sys
N, B = map(int,input().split())

li = []

def multiply(ll1,ll2):
    result = [[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += ll1[i][k] * ll2[k][j]
                result[i][j] %= 1000
    return result

def power(n):
    if n == 1:
        return li
    else:
        tmp = power(n//2)
        if n % 2 == 0:
            return multiply(tmp,tmp)
        else:
            return multiply(multiply(tmp,tmp),li)

for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        li[i][j] %= 1000

for i in power(B):
    print(*i)