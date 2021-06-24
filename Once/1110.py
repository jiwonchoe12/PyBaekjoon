n = int(input())
x = n
cnt = 1

A = x % 10
B = x // 10
C = (A+B)%10
x = x%10 * 10 + C

while(n != x):
    A = x % 10
    B = x // 10
    C = (A+B)%10
    x = x%10*10 + C
    cnt += 1
print(cnt)