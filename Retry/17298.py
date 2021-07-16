import sys

N = int(input())

li = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1] * N
for i in range(1,len(li)):
    if li[i-1] >= li[i]:
        stack.append([li[i-1],i-1])
    else:
        for j in range(len(stack)):
            if li[i] > stack[len(stack)-1][0]:
                result[stack.pop()[1]] = li[i]
            else:
                break
        result[i-1] = li[i]
for i in stack:
    result[i[1]] = -1
print(*result)