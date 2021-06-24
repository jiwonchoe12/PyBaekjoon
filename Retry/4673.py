a = [0 for i in range(1,10002)]
for i in range(1,10001):
    x = i
    n = i
    while x > 0:
        n += x%10
        x //= 10 
    if n <= 10000:
        a[n] += 1
for i in range(1,10001):
    if a[i] == 0:
        print(i)