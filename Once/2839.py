N = int(input())


def solve(a,b):
    n = 5*a + b*3
    if n > N:
        return
    if n == N:
        print(a+b)
        exit()
    solve(a+1,b)
    solve(a,b+1)
    

solve(0,0)
print(-1)