N = int(input())
N = 1000 - N
li = [500,100,50,10,5,1]

cnt = 0

for i in li:
    while i <= N or N == 0:
        if N == 0:
            print(cnt)
            exit()
        N -= i
        cnt += 1