import sys
from queue import PriorityQueue

que = PriorityQueue()

N = int(input())

result = []
for i in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        if que.qsize() == 0:
            print(0)
        else:
            print(-que.get())
    else:
        que.put(-tmp)
