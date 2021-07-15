from collections import deque
import sys

N = int(input())
li = deque()
stack = deque()
result = []
for i in range(N):
    li.append(int(sys.stdin.readline()))

for i in range(1,N+1):
    stack.append(i)
    result.append('+')
    while True:
        if len(stack) > 0 and stack[len(stack)-1] == li[0]:
            stack.pop()
            li.popleft()
            result.append('-')
        else:
            break
if len(li) == 0:
    print(*result,sep='\n')
else:
    print('NO')