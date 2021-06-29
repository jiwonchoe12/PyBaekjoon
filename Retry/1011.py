import math
N = int(input())

for i in range(N):
    X,Y = map(int,input().split())
    dis = Y-X
    m = int(math.sqrt(dis))
    if m*m == dis:
        cnt = m*2 - 1
        print(cnt)
        continue
    else:
        if dis <= m*m + m:
            cnt = m*2
            print(cnt)
            continue
        else:
            cnt = m * 2 + 1
            print(cnt)
            continue
