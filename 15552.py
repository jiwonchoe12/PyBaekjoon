import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    x,y = map(int, sys.stdin.readline().rstrip().split())
    print(x+y)
