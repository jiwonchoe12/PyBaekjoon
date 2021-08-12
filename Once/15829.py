N = int(input())

li = list(input().strip())

result = 0

for i in range(N):
    result += (ord(li[i]) - 96) * (31 ** i)
print(result % 1234567891)