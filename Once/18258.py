import sys
from collections import deque
li = deque()

def push(n):
    li.append(n)

def pop():
    if len(li) > 0:
        print(li[0])
        li.popleft()
    else:
        print(-1)

def size():
    print(len(li))

def empty():
    if len(li) > 0:
        print(0)
    else:
        print(1)

def front():
    if len(li) > 0:
        print(li[0])
    else:
        print(-1)
    
def back():
    if len(li) > 0:
        print(li[-1])
    else:
        print(-1)

T = int(input())

for i in range(T):
    X = list(sys.stdin.readline().split())
    if X[0] == 'push':
        push(X[1])
    elif X[0] == 'pop':
        pop()
    elif X[0] == 'size':
        size()
    elif X[0] == 'empty':
        empty()
    elif X[0] == 'front':
        front()
    elif X[0] == 'back':
        back()