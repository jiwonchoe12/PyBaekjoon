import sys
import math
T = int(input())
for i in range(T):
    li = []
    r_li = []
    x1,y1,r1,x2,y2,r2 = map(int, sys.stdin.readline().split())
    dis = (x1-x2)**2 + (y1-y2)**2
    sub1 = r2 + r1
    sub2 = r2 - r1
    sub1 **= 2
    sub2 **= 2
    if abs(dis) < sub1 and abs(dis) >sub2:
        print(2)
    elif abs(dis) == sub2 and dis != 0:
        print(1)
    elif abs(dis) == sub1:
        print(1)
    elif abs(dis) == 0 and r2==r1:
        print(-1)
    elif abs(dis) > sub1:
        print(0)
    elif abs(dis) < sub2:
        print(0)