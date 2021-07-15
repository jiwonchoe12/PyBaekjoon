N = int(input())

i = 5
cnt = 0
while True:
    if i > N:
        break
    cnt += N//i
    i *= 5
print(cnt)