T = int(input())

for i in range(T):
    N = int(input())
    d = {}
    for j in range(N):
        X,Y = map(str,input().split())
        if Y not in d:
            d[Y] = [X]
        else:
            d[Y].append(X)
    if len(d) == 1:
        for j in d:
            print(len(d[j]))
    else:
        cnt = 1
        for j in d:
            cnt *= (len(d[j])+1)
        print(cnt - 1)