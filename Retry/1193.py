X = 1
Y = 1
a_y = 2
a_x = 4
cnt = 1
flag = 0
N = int(input())
if N == 1:
    print('1/1')
    exit()
while True:
    X += 1
    Y += a_y
    cnt += 1
    if max(X,Y) >= N and min(X,Y) <= N:
        flag = 1
        break
    X += a_x
    Y += 1
    cnt += 1
    if max(X,Y) >= N and min(X,Y) <= N:
        flag = 2
        break
    a_y += 4
    a_x += 4
if flag == 2:
    print(max(X,Y) - N + 1, N - min(X,Y)+1,sep='/')
else:
    print( N - min(X,Y)+1,max(X,Y) - N + 1,sep='/')
