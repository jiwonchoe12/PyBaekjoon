import sys
N = int(input())
li = []
for i in range(N):
    li.append(list(sys.stdin.readline().split()))
li.sort(key = lambda x : int(x[0]))
for i in li:
    print(i[0],i[1])