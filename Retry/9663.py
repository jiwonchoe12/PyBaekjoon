N = int(input())
cnt = 0
def chk(li,x,y,to):
    x1 = x
    y1 = y
    for i in range(N):
        for j in range(N):
            li[y][j] += to
        li[i][x] += to
    while x1+1 < N and y1+1 < N:
        li[y1+1][x1+1] += to
        y1 += 1
        x1 += 1
    x1 = x
    y1 = y
    while x1-1 >= 0 and y1-1 >= 0:
        li[y1-1][x1-1] += to
        y1 -= 1
        x1 -= 1
    x1 = x
    y1 = y
    while x1+1 < N and y1-1 >= 0:
        li[y1-1][x1+1] += to
        y1 -= 1
        x1 += 1
    x1 = x
    y1 = y
    while x1-1 >= 0 and y1+1 < N:
        li[y1+1][x1-1] += to
        y1 += 1
        x1 -= 1
    return li

def prt(li):
    for i in range(N):
        for j in range(N):
            print(li[i][j], end= ' ')
        print()

def solve(depth,x,y,li):
    if x >= N or y >= N:
        return
    if lineY[y] == 1:
        return
    flag = 1
    for i in range(N):
        if lineX[i] == 1:
            continue
        if li[y][i] == 0:
            if depth == N:
                global cnt
                cnt += 1
                return
            li = chk(li,i,y,1)
            lineY[y] = 1
            lineX[i] = 1
            solve(depth+1, x+1,y+1,li)
            li = chk(li,i,y,-1)
            lineY[y] = 0
            lineX[i] = 0

r_li = [[0 for i in range(N)] for i in range(N)]
lineY = [0]*15
lineX = [0]*15
solve(1,0,0,r_li)
print(cnt)
