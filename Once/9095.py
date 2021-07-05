def solve(n):
    global N
    global cnt
    if n > N:
        return
    if n == N:
        cnt += 1
        return
    solve(n+1)
    solve(n+2)
    solve(n+3)

T = int(input())
for i in range(T):
    cnt = 0
    N = int(input())
    solve(0)
    print(cnt)