###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GOPPaAeMDFAXB&categoryId=AV7GOPPaAeMDFAXB&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-12
import sys
sys.stdin = open("input.txt")


def dfs(node, length):
    global maxNum
    visit[node] = True
    maxNum = max(maxNum, length)

    for neighbor in graph[node]:
        if not visit[neighbor]:
            dfs(neighbor, length + 1)

    visit[node] = False


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    visit = [False] * (N + 1)
    maxNum = 1
    for start in range(1, N + 1):
        dfs(start, 1)

    print(f"#{tc} {maxNum}")
