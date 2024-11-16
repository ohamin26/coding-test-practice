###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX4EJPs68IkDFARe&categoryId=AX4EJPs68IkDFARe&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=2
###  작성일 : 24-11-16
import sys

sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T + 1):
    N = input()
    minNum = int(N)
    maxNum = int(N)
    for i in range(len(N)):
        for j in range(i+1, len(N)):
            change = N[:i] + N[j] + N[i + 1:j] + N[i] + N[j + 1:]
            if change[0] == "0":
                continue
            change = int(change)
            minNum = min(change, minNum)
            maxNum = max(change, maxNum)
    print(f"#{tc} {minNum} {maxNum}")