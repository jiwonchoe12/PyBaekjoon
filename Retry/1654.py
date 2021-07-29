import sys
sys.setrecursionlimit(10**6)
K, N = map(int,input().split())

li = []

for i in range(K):
    li.append(int(sys.stdin.readline()))

li.sort()
start = 0
end = max(li)

while end-start >= 0:
    mid = (start+end) // 2
    if mid == 0:
        break
    lines = 0
    for i in li:
        lines += i // mid
    if lines >= N:
        start = mid+1
    else:
        end = mid -1

print(end)