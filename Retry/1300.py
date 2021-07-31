N = int(input())
K = int(input())

start = 1
end = N*N

while end - start >= 0:
    mid = (start + end) // 2
    s = 0
    for i in range(1,N+1):
        s += min(mid//i,N)
    if s < K:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)