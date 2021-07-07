while True:
    X = input()
    if X == '0':
        exit()
    if X == X[::-1]:
        print('yes')
    else:
        print('no')