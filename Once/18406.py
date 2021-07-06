X = input()

if sum(list(map(int,X[:len(X)//2].strip()))) == sum(list(map(int,X[len(X)//2:].strip()))):
    print('LUCKY')
else:
    print('READY')