###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7IzvG6EksDFAXB&categoryId=AV7IzvG6EksDFAXB&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-12
T = int(input())


def dfs(n, total):
    global answer
    if total > K:
        return
    if total == K:
        answer += 1
        return
    if n == N:
        return
    dfs(n+1, total+A[n])
    dfs(n+1, total)


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    answer = 0
    dfs(0,0)
    print(f"#{tc} {answer}")