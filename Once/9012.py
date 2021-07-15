T = int(input())

for i in range(T):
    x = input()
    x = x[::-1]
    st = 0
    for j in x:
        if j == ')':
            st += 1
        else :
            st -= 1
        if st < 0:
            break
    if st == 0:
        print('YES')
    else:
        print('NO')