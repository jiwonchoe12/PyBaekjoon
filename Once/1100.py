li = []
for i in range(8):
    li.append(list(map(str,input().strip())))
cnt = 0
for i in range(8):
    for j in range(i%2,8,2):
        if li[i][j] == 'F':
            cnt += 1
print(cnt)