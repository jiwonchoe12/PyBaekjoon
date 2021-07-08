import sys
li=[]
cnt =[]
N = int(input())

for i in range(N):
    li.append(list(map(int,sys.stdin.readline().split())))
    cnt.append([0 for j in range(i+1)])
cnt[0][0] = li[0][0]
for i in range(N-1):
    for j in range(len(li[i])):
        cnt[i+1][j] = max(cnt[i][j] + li[i+1][j],cnt[i+1][j])
        cnt[i+1][j+1] = max(cnt[i][j] + li[i+1][j+1],cnt[i+1][j+1])
print(max(cnt[len(cnt)-1]))