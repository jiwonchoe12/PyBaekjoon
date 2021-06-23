import sys
x,y = map(int , input().split())
li = []
chess = ['B', 'W']
result = 99999999

for i in range(x):
    li.append(list(sys.stdin.readline().strip()))


for i in range(x-7):
    for j in range(y-7):
        for c in range(2):
            chess = chess[::-1]
            r_li = []
            for a in range(8):
                tmp = []
                for b in range(8):
                    if a % 2 == 0:
                        tmp.append(chess[b%2])
                    else:
                        tmp.append(chess[(b+1)%2])
                r_li.append(tmp)
            cnt = 0
            for a in range(8):
                for b in range(8):
                    if li[i+a][j+b] != r_li[a][b]:
                        cnt += 1
            
            if result > cnt:
                result = cnt
print(result)