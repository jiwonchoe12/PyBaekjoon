T = int(input())

def solve(kk,n,li):
    global k
    r_li = []
    for i in range(n):
        r_li.append(sum(li[:i+1]))
    if k == kk:
        return r_li.pop()
    return solve(kk+1,n,r_li)

for i in range(T):
    k = int(input())
    n = int(input())
    r_li = []
    for j in range(n):
        r_li.append(j+1)
    print(solve(1,n,r_li))
    