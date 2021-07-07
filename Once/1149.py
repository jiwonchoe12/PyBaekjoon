import sys

N = int(input())
li = []
d = [[0,0,0]]
for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))
for i in range(1,N+1):
    r_li = []
    r_li.append(min(d[i-1][1],d[i-1][2]) + li[i-1][0])
    r_li.append(min(d[i-1][0],d[i-1][2]) + li[i-1][1])
    r_li.append(min(d[i-1][0],d[i-1][1]) + li[i-1][2])
    d.append(r_li)
print(min(d[N]))