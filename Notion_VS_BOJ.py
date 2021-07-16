import sys
li = list(map(int,sys.stdin.readlines())) # 노션 문제 입력
r_li = list(map(int,sys.stdin.readline().split())) # BOJ 문제 입력
for i in r_li:
    if i not in li:
        print(i)