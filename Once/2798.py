n, m = map(int, input().split())
li = list(map(int, input().split()))
result = []
for i in range(1,len(li)):
    for j in range(i+1, len(li)):
        for k in range(j+1, len(li)):
            a = li[i] + li[j] + li[k]
            if m - a >= 0:
                result.append(a)
            
print(max(result))
