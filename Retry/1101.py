N, M = map(int, input().split()) 
li = []
result =[]

for i in range(N):
    li.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if li[i][j] != 0:
            li[i][j] = 1

for k in range(len(li)):
    cnt = 0
    r_li = []
    for i in range(N):
        if k == i:
            continue
        if M - li[i].count(0) > 1:
            cnt += 1
        elif M - li[i].count(0) == 1:
            if li[i] not in r_li:
                r_li.append(li[i])
            else:
                cnt += 1
    result.append(cnt)
print(min(result))