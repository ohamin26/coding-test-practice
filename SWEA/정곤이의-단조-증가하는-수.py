###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWcPjEuKAFgDFAU4&categoryId=AWcPjEuKAFgDFAU4&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=2
###  작성일 : 24-11-14
import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, (input().split())))
    maxNum = -1
    for i in range(N):
        for j in range(i+1,N):
            cur = 0
            answer = True
            for z in str(A[i] * A[j]):
                if cur > int(z):
                    answer = False
                    break
                cur = int(z)
            if answer:
                maxNum = max(maxNum, A[i]*A[j])
    print(f"#{tc} {maxNum}")