import sys
N = int(input())
cost = []
for i in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))

ans = []
for a in range(3):
    r_li = [a]
    for i in range(1,N-2):
        mi = 0
        m = 9999
        for k in range(3):
            for j in range(3): 
                for z in range(3):
                    if k != z and k != j and r_li[i-1] != k:
                        if m > cost[i][k] + cost[i+1][j] + cost[i+2][z]:
                            m = cost[i][k] + cost[i+1][j] + + cost[i+2][z]
                            mi = k
        r_li.append(mi)
    m = 9999
    for i in range(3):
        for j in range(3):
            if i != r_li[len(r_li) - 2] and j != i:
                m = min(m,cost[N-2][i]+cost[N-1][j])
    s = m
    for i in range(len(r_li)):
        s+= cost[i][r_li[i]]
    ans.append(s)

    
print(min(ans))