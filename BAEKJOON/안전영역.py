###  문제 : https://www.acmicpc.net/problem/2468
###  작성일 : 24-11-16
import sys

sys.stdin = open("input.txt")

sys.setrecursionlimit(10000)
def dfs(n, x, y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[x][y] = True
    for dx, dy in directions:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and graph[nx][ny] >= n:
                dfs(n, nx, ny)

N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))


maxNum = 0
for i in range(1, 101):
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if not visited[x][y] and graph[x][y] >= i:
                dfs(i, x, y)
                cnt += 1
    maxNum = max(cnt, maxNum)
print(maxNum)
