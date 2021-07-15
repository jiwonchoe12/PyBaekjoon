import math
T = int(input())

for i in range(T):
    X,Y = map(int,input().split())
    print(math.factorial(Y) // (math.factorial(X)* math.factorial(Y-X)))