X = input()
li = []
tmp = 0
for i in range(len(X)):
    if X[i] == '-' or X[i] == '+':
        li.append(X[tmp:i])
        li.append(X[i])
        tmp = i+1
li.append(X[tmp:])
chk = [0] * len(li)
minus_sum = 0
plus_sum = 0

try:
    st = li.index('-')
    fi = 0
    for i in range(len(li)):
        if (li[i] == '-' or i == len(li)-1) and i != st:
            fi = i
            for j in range(st+1,fi+1,2):
                minus_sum += int(li[j])
                chk[j] = 1
            st = i
except:
    minus_sum = 0
for i in range(len(li)):
    if li[i] != '-' and li[i] != '+' and chk[i] == 0:
        plus_sum += int(li[i])
print(plus_sum - minus_sum)