N, K = map(int,input().split())
P = 1000000007
li = [[1]]

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i % P
    return result

def power(n, k):
    if k == 1:
        return n%P
    else:
        tmp = power(n,k//2)
        if k % 2 == 0:
            return tmp * tmp % P
        else:
            return tmp * tmp * n % P

print(factorial(N)*(power(factorial(K)*factorial(N-K),P-2))%P)