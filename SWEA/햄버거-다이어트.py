###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-11
import sys

sys.stdin = open("input.txt", "r")


def dfs(n, taste, kcal):
    global answer
    if kcal > L:
        return
    if taste > answer:
        answer = taste
    if n == N:
        return
    dfs(n+1, taste+info[n][0], kcal+info[n][1])
    dfs(n+1, taste, kcal)


T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    dfs(0, 0, 0)
    print(f"#{tc}",answer)