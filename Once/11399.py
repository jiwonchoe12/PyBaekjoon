import sys
N = int(input())

li = list(map(int,sys.stdin.readline().split()))

li.sort()
s = 0
for i in range(len(li)):
    s += sum(li[:i+1])
print(s)