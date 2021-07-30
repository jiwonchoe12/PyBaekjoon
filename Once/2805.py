import sys
N, M = map(int,input().split())

li = list(map(int,sys.stdin.readline().split()))

start = 0
end = max(li)

while end - start >= 0:
    mid = (start+end) // 2
    trees = 0
    for i in li:
        if i-mid > 0:
            trees += i-mid
            if trees > M:
                break
    if trees < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)