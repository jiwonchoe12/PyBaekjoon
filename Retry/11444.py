N = int(input())
X = [[1,1],[1,0]]
P = 1000000007

def multiply(x,y):
    result = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += x[i][k] * y[k][j]
                result[i][j] %= P
    return result

def power(n):
    if n == 1:
        return X
    else:
        tmp = power(n//2)
        if n % 2 == 0:
            return multiply(tmp,tmp)
        else:
            return multiply(multiply(tmp,tmp),X)
R = power(N)
print(R[1][0])