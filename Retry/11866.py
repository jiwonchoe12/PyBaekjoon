
k, n = map(int,input().split())
li = [i for i in range(1,k+1)]
cnt = -1
result = []
while len(li) > 0:
    cnt += n
    cnt = cnt%len(li)
    result.append(li.pop(cnt))
    cnt -= 1
print('<',end='')
print(*result,sep=', ',end='')
print('>',end='')
