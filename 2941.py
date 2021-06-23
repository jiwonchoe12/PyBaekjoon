li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

n = input()

for k in li:
    while n.find(k) != -1:
        n = n.replace(k,'a')
print(len(n))