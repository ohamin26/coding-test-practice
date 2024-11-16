###  문제 : https://www.acmicpc.net/problem/2606
###  작성일 : 24-11-16
N = int(input())
C = int(input())
computer = [list(map(int, input().split())) for _ in range(C)]
visited = [False for _ in range(N+1)]
graph = [[] for _ in range(N + 1)]
for x, y in computer:
    graph[x].append(y)
    graph[y].append(x)
cnt = 0
def dfs(n):
    global cnt
    visited[n] = True
    for node in graph[n]:
        if not visited[node]:
            cnt += 1
            dfs(node)
dfs(1)

print(cnt)