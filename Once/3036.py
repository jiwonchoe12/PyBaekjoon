import sys
import math
T = int(input())

li = list(map(int, sys.stdin.readline().split()))

for i in range(1,len(li)):
    lcm = math.lcm(li[0],li[i])
    print(lcm // li[i],'/', lcm // li[0], sep='')