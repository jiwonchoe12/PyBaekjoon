N = int(input())
li = [N] * (N*4)
li[0] = 0
for i in range(N+1):
    li[i*2] = min(li[i]+1,li[i*2])
    li[i*3] = min(li[i]+1,li[i*3])
    li[i+1] = min(li[i]+1,li[i+1])
print(li[N]-1)