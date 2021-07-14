import sys

N = int(input())

dis= list(map(int, sys.stdin.readline().split()))
cost=list(map(int, sys.stdin.readline().split()))
result = 0
tmp = 0
i = 0
for i in range(len(cost)):
    cnt = 0
    if i < tmp:
        continue
    for j in range(i+1,len(cost)):
        if cost[i] < cost[j]:
            cnt += dis[j-1]
            if j == len(cost)-1:
                result += cnt * cost[i]
                tmp = j
        else:
            cnt += dis[j-1]
            result += cnt * cost[i]
            tmp = j
            break
print(result)