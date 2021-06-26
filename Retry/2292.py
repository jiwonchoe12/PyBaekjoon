cnt = 1
li = [1]
N = int(input())
if N == 1:
    print(1)
    exit()
while True:
    li.append(li[len(li)-1] + 6*cnt)
    cnt+=1
    if li[len(li)-1] >= N:
        print(cnt)
        break