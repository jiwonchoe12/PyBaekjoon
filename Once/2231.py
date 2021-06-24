x = int(input())
for i in range(1,1000001):
    N = i
    n = i
    while N > 0:
        n += N % 10
        N //= 10
    if n == x:
        print(i)
        exit()
print(0)