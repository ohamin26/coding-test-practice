###  https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  참고한 내용 : https://velog.io/@seungjae/SWEA-1244.-SW-%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0-%EC%9D%91%EC%9A%A9-2%EC%9D%BC%EC%B0%A8-%EC%B5%9C%EB%8C%80-%EC%83%81%EA%B8%88-Python-%EC%99%84%EC%A0%84%ED%83%90%EC%83%89
###  작성일 : 24-11-05
import sys

sys.stdin = open("input.txt", "r")


def dfs(n):
    global answer
    if n == C:
        answer = max(answer, int("".join(map(str, arr))))
        return
    for i in range(L - 1):
        for j in range(i + 1, L):
            arr[i], arr[j] = arr[j], arr[i]
            chk = int("".join(map(str, arr)))
            if (n, chk) not in v:
                dfs(n + 1)
                v.append((n, chk))
            arr[j], arr[i] = arr[i], arr[j]
T = int(input())

for tc in range(1, T + 1):
    N, C = map(int, input().split())
    arr = list(str(N))
    C = int(C)
    L = len(str(N))
    v = []
    answer = 0
    dfs(0)
    print(f"#{tc}", answer)
