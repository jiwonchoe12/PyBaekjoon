import sys
N = int(input())
li = [0] * 10001
for i in range(N):
    tmp = int(sys.stdin.readline())
    li[tmp] += 1
for i in range(10001):
    for j in range(li[i]):
        sys.stdout.write(f'{i}\n')
