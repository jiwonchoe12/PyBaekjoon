li = [int(input()) for i in range(9)]

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if sum(li) - li[i] -li[j] == 100:
            print()
            r_li = []
            for k in range(len(li)):
                if k != i and k != j:
                    r_li.append(li[k])
            print(*sorted(r_li),sep='\n')
            exit()