###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWIsY84KEPMDFAWN&categoryId=AWIsY84KEPMDFAWN&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=2
###  작성일 : 24-11-14
import sys
from collections import deque

sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T + 1):
    C = input()
    words = []
    answer = {'S':0,'D':0,'H':0,'C':0}
    Error = False
    for i in range(0,len(C),3):
        word = C[i]+C[i+1]+C[i+2]
        if word in words:
            Error = True
            break
        words.append(word)
        answer[C[i]] += 1

    print(f"#{tc}", end=" ")
    if Error:
        print("ERROR")
    else :
        for v in answer:
            print(13-answer[v],end=" ")
        print("")
