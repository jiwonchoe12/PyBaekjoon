import sys
H,W = map(int,input().split())

li = list(map(int, sys.stdin.readline().split()))
s = 0
for i in range(1,len(li)-1):
    s+= max(min(max(li[:i])-li[i],max(li[i+1:])-li[i]),0)
print(s)