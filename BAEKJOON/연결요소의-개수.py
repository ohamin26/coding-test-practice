###  문제 : https://www.acmicpc.net/problem/11724
###  작성일 : 24-11-16
import sys

sys.stdin = open("input.txt")

def dfs(n):
    visited[n] = True
    for neighbor in graph[n]:
        if not visited[neighbor]:
            dfs(neighbor)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for i in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)