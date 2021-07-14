import sys
N = int(input())

li = []

for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))
li.sort(key= lambda x : (x[1],x[0]))
time = li[0][1]
cnt = 1
for i in range(1,len(li)):
    if li[i][0] >= time:
        cnt += 1
        time = li[i][1]

print(cnt)