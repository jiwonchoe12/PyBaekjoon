import math

N = int(input())
li = []
result = []
for i in range(N):
    li.append(int(input()))
tmp = li[0]
for i in range(len(li)):
    li[i] -= tmp
gcd = math.gcd(*li[1:])

for i in range(2,int(gcd**(1/2)) + 1):
    if gcd % i == 0:
        result.append(i)
        if i**2 != gcd:
            result.append(gcd // i)
result.append(gcd)
result.sort()
print(*result)