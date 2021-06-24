a = input()
d = {}

for k in a:
    if k in d:
        continue
    else:
        d[k] = a.index(k)
alpha = 'abcdefghijklmnopqrstuvwxyz'
for k in alpha:
    if k in d:
        print(d[k], end= ' ')
    else:
        print(-1, end=' ')
