import sys

class PriorityQueue:
    def __init__(self, SIZE = 300000):
        self.size = 0
        self.li = [None for i in range(SIZE)]
    
    def get_par_idx(self, child_idx):
        if child_idx != 1:
            if child_idx % 2 == 1:
                par = (child_idx - 1) // 2
            else:
                par = child_idx // 2
        else:
            par = None
        return par

    def get_small_child(self, par_idx):
        child1 = par_idx * 2
        child2 = par_idx * 2 + 1
        if self.li[child2] == None or self.li[child1] == None:
            if self.li[child1] == None:
                return None
            else:
                return child1
        if abs(self.li[child1]) == abs(self.li[child2]):
            if self.li[child1] < self.li[child2]:
                return child1
            else:
                return child2
        elif abs(self.li[child1]) < abs(self.li[child2]):
            return child1
        else:
            return child2

    def put(self, x):
        self.size += 1
        self.li[self.size] = x
        idx = self.size
        
        while idx != 1:
            par_idx = self.get_par_idx(idx)
            if par_idx:
                if abs(self.li[par_idx]) == abs(self.li[idx]) and self.li[par_idx] > self.li[idx]:
                    child = self.li[idx]
                    self.li[idx] = self.li[par_idx]
                    idx = par_idx
                    self.li[idx] = child
                elif abs(self.li[par_idx]) > abs(self.li[idx]):
                    child = self.li[idx]
                    self.li[idx] = self.li[par_idx]
                    idx = par_idx
                    self.li[idx] = child
                else:
                    break
    def pop(self):
        if self.size == 0:
            return 0
        tmp = self.li[1]
        self.li[1] = self.li[self.size]
        self.li[self.size] = None
        self.size -= 1
        idx = 1
        child = self.get_small_child(idx)
        while child != None:
            child = self.get_small_child(idx)
            if child:
                if abs(self.li[idx]) == abs(self.li[child]) and self.li[idx] > self.li[child]:
                    par = self.li[idx]
                    self.li[idx] = self.li[child]
                    idx = child
                    self.li[idx] = par
                elif abs(self.li[idx]) > abs(self.li[child]):
                    par = self.li[idx]
                    self.li[idx] = self.li[child]
                    idx = child
                    self.li[idx] = par
                else:
                    break

        return tmp

N = int(input())
que = PriorityQueue()
for i in range(N):
    X = int(sys.stdin.readline())
    if X == 0:
        print((que.pop()))
    else:
        que.put(X)
