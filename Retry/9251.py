A = ' ' + input()
B = ' ' + input()
li = [[0 for i in range(len(B))] for i in range(len(A))]
for i in range(1,len(A)):
    for j in range(1,len(B)):
        if A[i] == B[j]:
            li[i][j] = li[i-1][j-1] + 1
        else:
            li[i][j] = max(li[i-1][j],li[i][j-1])
print(li[-1][-1])
