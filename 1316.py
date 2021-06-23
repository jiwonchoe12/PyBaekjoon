N = int(input())
cnt = 0
for i in range(N):
    x = input()
    buff = ''
    li = []
    cnt += 1
    for k in x:
        if k not in li or k == buff:
            li.append(k)
            buff = k
        else:
            cnt -= 1
            break
print(cnt)