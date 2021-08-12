li = list(map(int, input().split()))
a,d = 1, 1

for i in range(len(li)):
    if i+1 != li[i]:
        a = 0
        break

for i in range(len(li),0,-1):
    if i != li[-i]:
        d = 0
        break
if a == 1:
    print('ascending')
elif d == 1:
    print('descending')
else:
    print('mixed')