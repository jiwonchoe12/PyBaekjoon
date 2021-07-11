import sys
N = int(input())
li = [int(sys.stdin.readline()) for i in range(N)]
li.sort()
for i in li:
    print(i)