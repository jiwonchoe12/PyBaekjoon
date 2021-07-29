import sys
N = int(input())
A = list(map(int,sys.stdin.readline().split()))
M = int(input())
B = list(map(int,sys.stdin.readline().split()))

A.sort()

for i in B:
    start = 0
    end = len(A)-1
    flag = 0
    while end - start > 0:
        mid = (start+end) //2
        if A[mid] == i or A[mid+1] == i:
            print(1)
            flag = 1
            break
        elif A[mid] > i:
            end = mid - 1
            continue
        elif A[mid] < i:
            start = mid + 1
            continue
    if flag == 0:
        print(0)