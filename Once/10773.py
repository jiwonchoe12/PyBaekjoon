import sys
T = int(input())
li = []
for i in range(T):
    X = int(sys.stdin.readline())
    if X == 0:
        li.pop()
    else:
        li.append(X)

print(sum(li))