A,B,C = map(int, input().split())

def solve(B):
    global A
    if B == 1:
        return A%C
    else:
        tmp = solve(B//2)
        if B % 2 == 0:
            return tmp * tmp % C
        else:
            return tmp* tmp* A % C
print(solve(B))
