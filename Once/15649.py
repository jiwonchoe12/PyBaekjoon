
n, m  = map(int,input().split())
def solve(depth,li):
    if depth == m:
        print(*li)
        return
    for i in range(n):
        if i+1 not in li:
            li.append(i+1)
            solve(depth+1,li)
            del li[len(li)-1]
        else:
            continue

for i in range(n):
    r_li = []
    r_li.append(i+1)
    solve(1,r_li)