import sys
N , M = map(int, input().split())

li = [i for i in range(1,N+1)]
r_li = list(map(int, sys.stdin.readline().split()))
p = 0
cnt = 0
for i in r_li:
    idx = li.index(i)
    A = abs((idx + (len(li)- p))%len(li))
    B = abs((p + (len(li)-idx))%len(li))
    if A > B:
        cnt += B
        li.pop(idx)
        p = idx
    else:
        cnt += A
        li.pop(idx)
        p = idx
print(cnt)