###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWVWgkP6sQ0DFAUO&categoryId=AWVWgkP6sQ0DFAUO&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=2
###  작성일 : 24-11-14
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    word = []
    maxLen = 0
    for i in range(5):
        ch =input()
        maxLen = max(len(ch), maxLen)
        word.append(ch)

    print(f"#{tc}", end=" ")
    for i in range(maxLen):
        for j in range(5):
            if len(word[j]) <= i:
                continue
            print(word[j][i], end="")

    print("")