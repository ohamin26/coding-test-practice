###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14yIsqAHYCFAYD&categoryId=AV14yIsqAHYCFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=2
###  작성일 : 24-11-14
import sys
from collections import deque
sys.stdin = open("input.txt")


for tc in range(1, 11):
    N = int(input())
    password = list(map(int, input().split()))
    C = int(input())
    command = list(map(str, input().split()))
    for i, v in enumerate(command):
        if v == "I":
            x = int(command[i + 1])
            y = int(command[i + 2])
            insert = deque()
            for j in range(i+3, i+y+3):
                insert.append(command[j])
            for z in range(x, x+y):
                change = int(insert.popleft())
                password.insert(z,change)
        elif v == "D":
            x = int(command[i + 1])
            y = int(command[i + 2])
            for z in range(y):
                if x < len(password):
                    del password[x]
    print(f"#{tc} ",*password[0:10])