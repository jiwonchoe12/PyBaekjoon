def make_star(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + ' ' * len(n) + n[i%len(n)])
        else:
            matrix.append(n[i%len(n)] * 3)
    return matrix

n = int(input())
e = 0
star = ['***', '* *', '***']
while n != 3:
    e += 1
    n //= 3

for i in range(e):
    star = make_star(star)
for i in star:
    print(i)