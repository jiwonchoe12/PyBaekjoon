x = 1
arr = [0 for i in range(10)]
for i in range(3):
    x *= int(input())
while x > 0:
    arr[x%10] += 1
    x //= 10

for i in arr:
    print(i)