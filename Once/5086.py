import sys

while True:
    X,Y = map(int, sys.stdin.readline().split())
    if X == 0 and Y == 0:
        break
    if Y % X == 0:
        print('factor')
        continue
    if X % Y == 0:
        print('multiple')
        continue
    print('neither')