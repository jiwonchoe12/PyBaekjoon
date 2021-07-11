import sys
N = int(input())
li = list(map(int,sys.stdin.readline().split()))

length = [0] * N
length2 = [0] * N
for i in range(N):
    length[i] = 1
    for j in range(0,i):
        if li[i] > li[j]:
            length[i] = max(length[i], length[j]+1)
li.reverse()
for i in range(N):
    length2[i] = 1
    for j in range(0,i):
        if li[i] > li[j]:
            length2[i] = max(length2[i], length2[j]+1)
length2.reverse()
ans = 0
for i in range(N):
    ans = max(ans,length[i] + length2[i])
print(ans-1)