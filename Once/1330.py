x, y = map(int, input().split())

print((lambda a, b : '>' if a > b else('==' if a==b else('<')))(x,y))
