import sys
N = int(input())
li = []
for i in range(N):
    li.append(sys.stdin.readline().rstrip())
li = list(set(li))
li.sort(key= lambda x : (len(x),x))
for i in li:
    print(i)