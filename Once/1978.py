def is_prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

N = int(input())
li = list(map(int, input().split()))
cnt = 0
for i in li:
    if is_prime(i):
        cnt += 1
print(cnt)