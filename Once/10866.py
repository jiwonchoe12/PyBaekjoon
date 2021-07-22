import sys
class Deque:
    def __init__(self):
        self.li = []
    def push_front(self, x):
        r_li = [0]
        r_li += self.li[:]
        r_li[0] = x
        self.li = r_li[:]
    def push_back(self, x):
        self.li.append(x)
    def pop_front(self):
        if len(self.li) > 0:
            tmp = self.li[0]
            self.li = self.li[1:]
            return tmp
        else:
            return -1
    def pop_back(self):
        if len(self.li) > 0:
            return self.li.pop()
        else:
            return -1
    def size(self):
        return len(self.li)
    def empty(self):
        if len(self.li) > 0:
            return 0
        else:
            return 1
    def front(self):
        if len(self.li) > 0:
            return self.li[0]
        else:
            return -1
    def back(self):
        if len(self.li) > 0:
            return self.li[-1]
        else:
            return -1

q = Deque()

T = int(input())

for i in range(T):
    X = list(sys.stdin.readline().split())
    if X[0] == 'push_back':
        q.push_back(int(X[1]))
    elif X[0] == 'push_front':
        q.push_front(int(X[1]))
    elif X[0] == 'pop_front':
        print(q.pop_front())
    elif X[0] == 'pop_back':
        print(q.pop_back())
    elif X[0] == 'size':
        print(q.size())
    elif X[0] == 'empty':
        print(q.empty())
    elif X[0] == 'front':
        print(q.front())
    elif X[0] == 'back':
        print(q.back())