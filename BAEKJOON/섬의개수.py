###  문제 : https://www.acmicpc.net/problem/4963
###  작성일 : 24-11-16
import sys

sys.stdin = open("input.txt")


def dfs(x, y):
    if not (0 <= x < H and 0 <= y < W) or visited[x][y] or land[x][y] == 0:
        return
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in directions:
        dfs(x + dx, y + dy)


while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    land = []
    visited = [[False for _ in range(W)] for _ in range(H)]
    for _ in range(H):
        land.append(list(map(int, input().split())))
    cnt = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and land[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)