x = input()

li = []
for i in x:
    li.append(int(i))
li.sort(reverse=True)
for i in li:
    print(i,end='')