class PriorityQueue:
    def __init__(self):
        MAX = 1024
        self.li = [None for i in range(MAX)]
        self.size = 0
    
    def put(self, x):
        self.size += 1
        