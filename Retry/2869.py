import math
A, B, V = map(int, input().split())
cnt = 1
V -= A
cnt += math.ceil(V / (A - B))
print(cnt)