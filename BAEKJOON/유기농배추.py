###  문제 : https://www.acmicpc.net/problem/1012
###  작성일 : 24-11-16
import sys

sys.stdin = open("input.txt")
sys.setrecursionlimit(10000)

def dfs(x, y):
    visited[y][x] = True
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < M and 0 <= ny < N:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny)


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    cnt = 0
    for k in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                cnt += 1
    print(cnt)