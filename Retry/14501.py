import sys
D = int(input())

li = [list(map(int, sys.stdin.readline().split())) for i in range(D)]
result = [0] * (D+1)
for i in range(D-1, -1, -1):
    if li[i][0] + i > D:
        result[i] = result[i+1]
        continue
    if li[i][1] + result[i+li[i][0]] > result[i+1]:
        result[i] = li[i][1] + result[i+li[i][0]]
    else:
        result[i] = result[i+1]
print(max(result))
