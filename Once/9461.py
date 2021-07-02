d = {}
d[1] = 1
d[2] = 1
d[3] = 1
T = int(input())
for k in range(T):
    X = int(input())
    if X in d:
        print(d[X])
        continue
    for i in range(4,X+1):
        d[i] = d[i-3] + d[i-2]
    print(d[X])