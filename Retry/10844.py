N = int(input())
li = [[0,1,1,1,1,1,1,1,1,1]]

for i in range(1,N):
    r_li = [0]*10
    for j in range(10):
        if j == 0:
            r_li[j] = li[i-1][j+1]
        elif j == 9:
            r_li[j] = li[i-1][j-1]
        else:
            r_li[j] = li[i-1][j+1] + li[i-1][j-1]
    li.append(r_li)
print(sum(li.pop())%1000000000)