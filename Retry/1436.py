N = int(input())
li = []
cnt = 0
data = 666
while True:
    if '666' in str(data):
        cnt += 1
    if N == cnt:
        print(data)
        break
    data += 1