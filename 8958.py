import sys
n = int(input())
for i in range(n):
    x = sys.stdin.readline()
    score = 1
    result = 0
    for j in x:
        if j == 'O':
            result += score
            score += 1
        else:
            score = 1
    print(result)