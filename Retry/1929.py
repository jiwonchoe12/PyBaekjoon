import sys
M,N = map(int, input().split())
li = [0] * 1000010
li[1] = 1
for i in range(2,10000):
    for j in range(i+i,1000001,i):
        li[j] = 1

for i in range(M,N+1):
    if li[i] == 0:
        sys.stdout.write(str(i))
        sys.stdout.write('\n')
