N = int(input())
cnt = 0
for i in range(1,N+1):
    if i < 100:
        cnt += 1
    else:
        buff = str(i)
        if int(buff[1]) - int(buff[0]) == int(buff[2]) - int(buff[1]):
            cnt += 1
print(cnt)
