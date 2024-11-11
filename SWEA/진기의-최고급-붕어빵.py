###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV5LsaaqDzYDFAXc&categoryId=AV5LsaaqDzYDFAXc&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-11
import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    state = "Possible"
    for i in range(len(P)):
        count = (P[i] // M) * K
        if count < i+1:
            state = "Impossible"
            break
    print(f"#{tc}",state)