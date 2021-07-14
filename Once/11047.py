N, K = map(int,input().split())
li = []
for i in range(N):
    li.append(int(input()))
cnt = 0
li.sort(reverse=True)
for i in li:
    tmp = K // i
    K -= tmp * i
    cnt += tmp
print(cnt)