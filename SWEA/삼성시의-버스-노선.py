###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWczm7QaACgDFAWn&categoryId=AWczm7QaACgDFAWn&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-14
import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    P = int(input())
    print(f"#{tc}", end=" ")
    for i in range(P):
        C = int(input())
        cnt = 0
        for j in range(N):
            a = A[j]
            b = B[j]
            if a <= C <= b:
                cnt += 1
        print(cnt, end=" ")
    print("")