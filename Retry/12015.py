import sys

N = int(input())
li = list(map(int,sys.stdin.readline().split()))

W = []
W.append(li[0])

def binary_search(x):
    start = 0
    end = len(W)-1

    while end-start > 0:
        mid = (start+end) // 2
        if W[mid] < x:
            start = mid + 1
        else:
            end = mid
    return end

for i in range(1,N):
    if W[-1] < li[i]:
        W.append(li[i])
    else:
        idx = binary_search(li[i])
        W[idx] = li[i]
    
print(len(W))