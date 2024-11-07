###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GKs06AU0DFAXB&categoryId=AV7GKs06AU0DFAXB&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-07
import sys

sys.stdin = open("input.txt", "r")

T = int(input())


def check(row):
    for i in range(row):
        if v[row] == v[i] or row - i == abs(v[row] - v[i]):
            return False
    return True


def dfs(n):
    global answer
    if n == N:
        answer += 1
        return

    for i in range(N):
        v[n] = 1
        if check(n):
            dfs(n + 1)


for tc in range(1, T + 1):
    N = int(input())
    v = [0 for _ in range(N)]
    answer = 0
    dfs(0)
    print(f"#{tc}", answer)
