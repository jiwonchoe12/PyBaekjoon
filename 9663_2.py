N = int(input())

cnt = 0

def solve(depth):
    global cnt
    if depth == N:
        cnt +=1
        return
    for i in range(N):
        if i in queen:
            continue

        flag = 1
        for k in range(len(queen)):
            if abs(k-depth) == abs(queen[k] - i):
                flag = 0
                break
        if flag:
            queen.append(i)
            solve(depth+1)
            del queen[len(queen)-1]


queen = []
solve(0)
print(cnt)