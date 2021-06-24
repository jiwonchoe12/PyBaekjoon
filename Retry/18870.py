import sys
N = int(input())
li = list(map(int,sys.stdin.readline().split()))
r_li = list(set(li))
r_li.sort()
r_li = {r_li[i]: i for i in range(len(r_li))}
print(*[r_li[i] for i in li])
    