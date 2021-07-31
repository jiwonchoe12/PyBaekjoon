import sys
N, M = map(int,input().split())
li = []
for i in range(N):
    li.append(int(sys.stdin.readline().rstrip()))
li.sort()

start = 1
end = li[-1]
result = 0
while end - start >= 0:
    mid = (start+end) // 2
    tmp = li[0]
    cnt = 1
    for i in range(1,N):
        d = li[i] - tmp
        if mid <= d:
            cnt += 1
            tmp = li[i]
    if cnt >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)