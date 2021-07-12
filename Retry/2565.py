N= int(input())
li = []
length = [0] * N

for i in range(N):
    li.append(list(map(int,input().split())))
li.sort(key = lambda x : x[0])
for i in range(N):
    length[i] = 1
    for j in range(0,i):
        if li[i][1] > li[j][1]:
            length[i] = max(length[j]+1,length[i])
print(N-max(length))