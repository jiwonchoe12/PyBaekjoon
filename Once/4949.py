import sys

while True:
    x = sys.stdin.readline().rstrip()
    if len(x) == 1:
        break
    x = x[::-1]
    st1 = 0
    st2 = 0
    flag = 1
    tmp = []
    for i in x:
        if i == ')' or i == ']':
            tmp.append(i)
        if i == ')':
            st1 += 1
        elif i == '(':
            if len(tmp) > 0:
                if tmp[len(tmp)-1] != ')':
                    flag = 0
                    break
                tmp.pop()
            st1 -= 1
        elif i == ']':
            st2 += 1
        elif i == '[':
            if len(tmp) > 0 :
                if tmp[len(tmp)-1] != ']':
                    flag = 0
                    break
                tmp.pop()
            st2 -= 1
        if st1 < 0 or st2 < 0:
            break
    if st2 == 0 and st1 == 0 and flag == 1:
        print('yes')
    else:
        print('no')
