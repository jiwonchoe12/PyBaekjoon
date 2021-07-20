import sys
from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    li = list(map(int, sys.stdin.readline().split()))
    q = deque()
    for i,v in enumerate(li):
        q.append([v,i])
    cnt = 0
    m = max(q, key=lambda x : x[0])[0]
    while len(q) > 0:
        tmp = q.popleft()
        if tmp[0] >= m:
            cnt += 1
            if tmp[1] == M:
                break
            if len(q) > 0:
                m = max(q, key=lambda x : x[0])[0]
        else:
            q.append(tmp)
    print(cnt)