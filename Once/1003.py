def fibo(n):
    if n == 0:
        d[0] = [0,1,0]
        return 0
    elif n == 1:
        d[1] = [0,0,1]
        return 1
    elif n in d:
        return d[n][0]
    else:
        d[n] = [fibo(n-1) + fibo(n-2),d[n-1][1] + d[n-2][1], d[n-1][2] +d[n-2][2]]
        return d[n][0]
T = int(input())
fibo(40)
d = {}
for i in range(T):
    X = int(input())
    print(d[X][1],d[X][2])