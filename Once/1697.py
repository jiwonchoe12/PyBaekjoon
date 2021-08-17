from collections import deque

S,T = map(int, input().split())
li = [999999] * 100001
li[S] = 0
que = deque()
que.append(S)
def BFS(s):
    while que:
        for i in range(len(que)):
            x = que.popleft()
            if x == T:
                return
            if x + 1 <= 100000 and li[x] + 1 < li[x+1]:
                li[x+1] = li[x]+1
                que.append(x+1)
            if x - 1 >= 0 and li[x] + 1 < li[x-1]:
                li[x-1] = li[x] + 1
                que.append(x-1)
            if x*2 <= 100000 and li[x] + 1 < li[x*2]:
                li[x*2] = li[x] + 1
                que.append(x*2)

BFS(S)
print(li[T])