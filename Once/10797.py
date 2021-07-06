D = int(input())

li = list(map(int,input().split()))
D %= 10
cnt = 0
for i in li:
    if D == i:
        cnt += 1
print(cnt)