import math
import sys
sys.setrecursionlimit(10**6)

def init(node, start, end):
    if start == end:
        tree[node] = start
        return
    mid = (start+end) //2
    init(node * 2, start,mid)
    init(node * 2 + 1, mid+1,end)
    if(arr[tree[node*2]] <= arr[tree[node*2 +1]]):
        tree[node] = tree[node * 2]
    else:
        tree[node] = tree[node*2+1]

def query(node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start+end) //2
    m1 = query(node*2, start, mid, left, right)
    m2 = query(node*2+1, mid+1, end, left, right)

    if m1 == -1:
        return m2
    elif m2 == -1:
        return m1
    
    else:
        if arr[m1] <= arr[m2]:
            return m1
        else:
            return m2

def getmax(start,end):
    n = len(arr)
    m = query(1,0,n-1,start,end)
    area = (end-start+1)*arr[m]

    if start <= m-1:
        tmp = getmax(start,m-1)
        if area < tmp:
            area = tmp

    if m+1 <= end:
        tmp = getmax(m+1,end)
        if area < tmp:
            area = tmp
    
    return area

while True:
    arr = list(map(int,sys.stdin.readline().split()))
    if arr[0] == 0:
        break
    arr = arr[1:]
    h = int(math.ceil(math.log2(len(arr))))
    size = pow(2,(h+1))
    tree = [0 for i in range(size+1)]
    init(1,0,len(arr)-1)
    print(getmax(0,len(arr)-1))