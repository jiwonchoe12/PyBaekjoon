import sys
d = {}

d[0] = 0
d[1] = 1
N = int(input())
for i in range(2,N+2):
    d[i] = d[i-1] + d[i-2]
    d[i] %= 15746
print(d[N+1])