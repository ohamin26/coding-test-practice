###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXaSUPYqPYMDFASQ&categoryId=AXaSUPYqPYMDFASQ&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-14
import sys
sys.stdin = open("input.txt")

T = int(input())


def checkCol(num,x):
    global answer
    cnt = 0
    if x > N-5:
        return
    for i in range(x,x+5):
        if board[num][i] == 'o':
            cnt += 1
    if cnt == 5:
        answer = "YES"


def checkRow(num,y):
    global answer
    cnt = 0
    if y > N-5:
        return
    for i in range(y,y+5):
        if board[i][num] == 'o':
            cnt += 1
    if cnt == 5:
        answer = "YES"


def checkCross(x,y):
    global answer
    cntR = 0
    cntL = 0
    for i in range(5):
        if x+i < N and y+i < N and board[x+i][y+i] == 'o':
            cntR += 1
        if x+i < N and y-i >= 0 and board[x+i][y-i] == 'o':
            cntL += 1
    if cntL == 5 or cntR == 5:
        answer = "YES"


for tc in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]
    answer = "NO"
    for i in range(N):
        for j in range(N):
            checkCol(i, j)
            checkRow(j, i)
            checkCross(i, j)

    print(f"#{tc} {answer}")