import sys
N = int(input())

i = 2
while N != 1:
    if N % i == 0:
        sys.stdout.write(str(i))
        sys.stdout.write('\n')
        N //= i
    else:
        i+=1