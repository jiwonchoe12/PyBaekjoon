arr = [0 for i in range(42)]
cnt = 0
for i in range(10):
    x = int(input())%42
    if arr[x] == 0:
        cnt += 1
    arr[x] += 1
print(cnt)