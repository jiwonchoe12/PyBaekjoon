import sys
N = int(input())
li = list(map(int,input().split()))
oper = list(map(int,input().split())) # + - * /

M, m = -sys.maxsize, sys.maxsize

def solve(num, depth):
    global M, m
    if depth == N:
        if num > M:
            M = num
        if num < m:
            m = num
        return
    for k in range(4):
        if oper[k] > 0:
            if k == 0:
                oper[k] -= 1
                solve(num + li[depth], depth+1)
                oper[k] += 1
            elif k == 1:
                oper[k] -= 1
                solve(num - li[depth], depth+1)
                oper[k] += 1
            elif k == 2:
                oper[k] -= 1
                solve(num * li[depth], depth+1)
                oper[k] += 1
            else:
                oper[k] -= 1
                if num < 0:
                    solve(-(-num // li[depth]), depth+1)
                else:
                    solve(num // li[depth], depth+1)
                oper[k] += 1
solve(li[0],1)
print(M)
print(m)