import sys
n, x = map(int, input().split())
a = sys.stdin.readline().rstrip().split()
for i in a:
    if int(i) < x:
        print(i, end= ' ')