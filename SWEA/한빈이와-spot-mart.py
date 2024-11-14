###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AW8Wj7cqbY0DFAXN&categoryId=AW8Wj7cqbY0DFAXN&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-12
import sys
sys.stdin = open("input.txt")

T = int(input())


def dfs(n, weight, cnt):
    global maxWeight
    if cnt == 2:
        if weight <= M:
            maxWeight = max(maxWeight, weight)
        return
    if n >= N:
        return
    if weight > M:
        return
    dfs(n+1, weight+a[n], cnt+1)
    dfs(n+1, weight, cnt)


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    maxWeight = -1
    dfs(0,0,0)
    print(f"#{tc} {maxWeight}")