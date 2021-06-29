import sys
li = [0] * 10001
li[1] = 1
for i in range(2,100):
    for j in range(i+i,10000,i):
        li[j] += 1

N = int(input())
for i in range(N):
    X = int(sys.stdin.readline())
    dis = 9999999
    m = 0
    for k in range(X+1):
        if li[X - k] == 0 and li[k] == 0:
            if abs((X-k)-k) < dis:
                dis = abs((X-k)-k)
                m = k
    print(*sorted([m,X-m]))