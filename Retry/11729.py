n = int(input())
cnt = 0
li = []
def hanoi(n, fro, to, tmp):
    global cnt
    if n == 1:
        li.append((fro,to))
        cnt += 1
    else:
        hanoi(n-1,fro, tmp, to)
        li.append((fro,to))
        cnt += 1
        hanoi(n-1, tmp, fro, to)

hanoi(n,1,2,3)
print(cnt)
for k in li:
    print(k[0],k[1])