import sys
from collections import deque

class AC:
    def __init__(self):
        self.li = deque()
        self.direction = 1
    
    def R(self):
        self.direction *= -1
    
    def D(self):
        if len(self.li) > 0:
            if self.direction == 1:
                self.li.popleft()
            else:
                self.li.pop()
            return 1
        else:
            return 0

T = int(input())

for i in range(T):
    flag = 1
    X = AC()
    order = sys.stdin.readline().strip()
    N = int(input())
    Y = sys.stdin.readline().strip()
    Y = Y.replace('[', '')
    Y = Y.replace(']','')
    X.li = deque(Y.split(','))
    if X.li[0] == '':
        X.li.popleft()
    for k in order:
        if k == 'R':
            X.R()
        if k == 'D':
            if not X.D():
                print('error')
                flag = 0
                break
    if X.direction == -1:
        X.li.reverse()
    if flag:
        print('[',end='')
        print(*X.li,sep=',',end='')
        print(']')