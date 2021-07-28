import sys
def dis(X,Y):
    return (X[0]-Y[0]) **2 + (X[1]-Y[1]) ** 2

def brute(start, end):
    m = sys.maxsize
    for i in range(start,end):
        for j in range(i+1,end+1):
            m = min(dis(li[i],li[j]),m)
    return m

def closest(start, end):
    if end-start +1 < 4:
        return brute(start,end)
    
    mid = (start+end)//2

    left = closest(start,mid)
    right = closest(mid+1, end)

    m = min(left,right)
    band = middleband(start,mid,end,m)
    return min(m,band)

def middleband(start,mid,end,m):
    midx = li[mid][0]
    ll = []
    for i in range(start,end+1):
        xdist = li[i][0] - midx

        if xdist ** 2 < m:
            ll.append(li[i])
    
    ll.sort(key=lambda x : x[1])
    for i in range(len(ll)-1):
        for j in range(i+1,len(ll)):
            ydist = ll[i][1] - ll[j][1]
            if ydist ** 2 < m:
                m = min(dis(ll[i],ll[j]),m)
            else:
                break
    return m


N = int(input())
li = []
for i in range(N):
    li.append(list(map(int,sys.stdin.readline().split())))

li.sort(key= lambda x : x[0])
print(closest(0,N-1))