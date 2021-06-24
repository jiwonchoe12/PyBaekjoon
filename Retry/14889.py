import sys
N = int(input())
length = N//2
li = []
r_li = []
m = []

def cal_score(link):
    start = [i for i in range(N)]
    start = list(set(start) - set(link))
    s_start = 0
    s_link = 0
    for i in range(0,length):
        for j in range(i+1,length):
            s_start += li[start[i]][start[j]] + li[start[j]][start[i]]
            s_link += li[link[j]][link[i]] + li[link[i]][link[j]]
    return abs(s_link - s_start)

def solve(num):
    global m
    if len(r_li) == length:
        m.append(cal_score(r_li))
        return
    for i in range(num,N):
        if i not in r_li:
            r_li.append(i)
            solve(i)
            del r_li[len(r_li)-1]
    

for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))

solve(0)
print(min(m))