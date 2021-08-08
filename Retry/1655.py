import heapq
import sys

left = []
right = []
N = int(input())

for i in range(N):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))
    if len(left) >= 1 and len(right) >= 1 and left[0][1] > right[0][1]:
        max_value = heapq.heappop(left)[1]
        min_value = heapq.heappop(right)[1]
        heapq.heappush(left, (-min_value, min_value))
        heapq.heappush(right, (max_value, max_value))
    print(left[0][1])