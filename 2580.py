import sys
li = []

def prt(li):
    for i in range(9):
        for j in range(9):
            print(li[i][j],end = ' ')
        print()
def solve(cnt):
    if cnt == N:
        prt(li)
        exit()
    i, j = XY_list[cnt][0], XY_list[cnt][1]
    r_li = []
    rr_li = []
    ri = i // 3
    rj = j // 3
    for a in range(ri*3,ri*3+3):
        for b in range(rj*3,rj*3+3):
            rr_li.append(li[a][b])
    for k in range(9):
        r_li.append(li[k][j])
    for k in range(1,10):
        if k not in li[i] and k not in r_li and k not in rr_li:
            li[i][j] = k
            solve(cnt+1)
            li[i][j] = 0

for i in range(9):
    li.append(list(map(int, sys.stdin.readline().split())))
N = 0
XY_list = []
for i in range(9):
    for j in range(9):
        if li[i][j] == 0:
            XY_list.append((i,j))
            N += 1
solve(0)
