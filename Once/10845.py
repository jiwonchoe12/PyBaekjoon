import sys
from collections import deque
N = int(input())

que = deque()

for i in range(N):
    X = list(sys.stdin.readline().split())
    if X[0] == 'push':
        que.append(X[1])
    elif X[0] == 'front':
        if len(que) > 0:
            print(que[0])
        else:
            print(-1)
    elif X[0] == 'size':
        print(len(que))
    elif X[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif X[0] == 'back':
        if len(que) > 0:
            print(que[-1])
        else:
            print(-1)
    elif X[0] == 'pop':
        if len(que) > 0:
            print(que.popleft())
        else:
            print(-1)