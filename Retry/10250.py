n = int(input())
for i in range(n):
    H,W,N = map(int,input().split())
    cnt = 0
    for k in range(W):
        for j in range(H):
            cnt += 1
            if cnt == N:
                print(f'{j+1}%s'% str(k+1).zfill(2))