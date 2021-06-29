import sys

while True:
    li = list(map(int, sys.stdin.readline().split()))
    li.sort()
    if li[0] == 0 and li[1] == 0 and li[2] == 0:
        break

    if li[0]*li[0] + li[1]*li[1] == li[2]*li[2] and li[0] + li[1] > li[2]:
        print('right')
    else:
        print('wrong')