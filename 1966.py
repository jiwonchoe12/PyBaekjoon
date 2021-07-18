import sys
from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    li = deque(map(int, sys.stdin.readline().split()))
    q = deque()
    m = max(li)
    while len(li) > 0:
        tmp = li.popleft()
        if tmp >= m:
            if len(li) > 0:
                m = max(li)
        else:
            li.append(tmp)
    