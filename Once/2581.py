def is_prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

M = int(input())
N = int(input())
li = []
for i in range(M,N+1):
    if is_prime(i):
        li.append(i)
if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(li[0])