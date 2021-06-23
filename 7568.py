N = int(input())
li = []
for i in range(N):
    li.append(list(map(int, input().split())))
    li[i].append(0)
for i in range(len(li)):
    for j in range(len(li)):
        if i != j and li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            li[i][2] += 1
for k in li:
    print(k[2]+1, end = ' ')