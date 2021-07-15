import math

n,k = map(int,input().split())
li = [[0 for i in range(n+1)] for i in range(n+1)]
if k > n or k< 0:
    print(0)
else:
    for i in range(1,n+1):
        for j in range(k+1):
            if i == j:
                li[i][j] = 1
            elif j == 0:
                li[i][j] = 1
            else:
                li[i][j] = (li[i-1][j-1] + li[i-1][j]) % 10007
print(li[n][k])