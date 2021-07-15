X , Y = map(int,input().split())

def count(n,num):
    i = num
    cnt = 0
    while True:
        if i > n:
            break
        cnt += n // i
        i *= num
    return cnt


five = count(X,5) - count(Y,5) - count(X-Y,5)
two = count(X,2) - count(Y,2) - count(X-Y,2)
print(min(five,two))