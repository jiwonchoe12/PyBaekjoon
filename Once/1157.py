a = input()
a = a.upper()
d = {}
for k in a:
    if k in d:
        d[k] += 1
    else:
        d[k] = 1
m = 0
result = ''
for k in d:
    if d[k] > m:
        m = d[k]
        result = k
    elif d[k] == m:
        result = '?'
print(result)