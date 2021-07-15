import sys
N = int(input())
li = []

def push(n):
    li.append(n)
def pop():
    if len(li)>0:
        print(li[len(li)-1])
        del li[len(li)-1]
    else:
        print(-1)
def size():
    print(len(li))

def empty():
    if len(li) > 0:
        print(0)
    else:
        print(1)

def top():
    if len(li)>0:
        print(li[len(li)-1])
    else:
        print(-1)

for i in range(N):
    X = list(sys.stdin.readline().split())
    if X[0] == 'push':
        push(int(X[1]))
    elif X[0] == 'pop':
        pop()
    elif X[0] == 'top':
        top()
    elif X[0] == 'size':
        size()
    elif X[0] == 'empty':
        empty()