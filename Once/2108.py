import sys
N = int(input())
li = []
r_li = []
d = {}
for i in range(N):
    tmp = int(sys.stdin.readline())
    li.append(tmp)
    if tmp in d:
        d[tmp] += 1
    else:
        d[tmp] = 1
val = d.values()
max_val = max(val)
for i in d:
    if d[i] == max_val:
        r_li.append(i)
r_li.sort()
li.sort()
print(round(sum(li) / len(li)))
print(li[len(li)//2])
if len(r_li) == 1:
    print(r_li[0])
else:
    print(r_li[1])

print(max(li)- min(li))