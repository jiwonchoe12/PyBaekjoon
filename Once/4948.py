import math
li = [0] * 300000
li[1] = 1 
for i in range(2,int(math.sqrt(300000))):
    for j in range(i+i, 300000, i):
        li[j] += 1

while True:
    N = int(input())
    if N == 0:
        break
    s = 0
    for i in range(N+1,2*N+1):
        if li[i] == 0:
            s += 1
    print(s)
