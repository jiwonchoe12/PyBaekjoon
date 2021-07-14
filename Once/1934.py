T = int(input())

def gcd(x,y):
    tmp = x % y
    if tmp == 0:
        return y
    x = y
    y = tmp
    return gcd(x,y)

for i in range(T):
    X,Y = map(int, input().split())
    print(X*Y // gcd(max(X,Y),min(X,Y)))