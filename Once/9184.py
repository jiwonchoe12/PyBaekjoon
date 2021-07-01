import sys
d = {}
def w(a,b,c):
    if (a,b,c) in d:
        return d[(a,b,c)]
    if a<= 0 or b <= 0 or c <= 0:
        d[(a,b,c)] = 1
        return 1
    if a > 20 or b > 20 or c > 20:
        d[(a,b,c)] = w(20,20,20)
        return d[(a,b,c)]
    if a < b and b < c:
        d[(a,b,c)] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return d[(a,b,c)]
    else:
        d[(a,b,c)] =  w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        return d[(a,b,c)]

while True:
    x,y,z = map(int, sys.stdin.readline().split())
    if x == -1 and y == -1 and z == -1:
        break
    result = w(x,y,z)
    print(f'w({x}, {y}, {z}) = {result}')