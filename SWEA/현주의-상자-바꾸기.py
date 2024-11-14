###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWYygN36Qn8DFAVm&categoryId=AWYygN36Qn8DFAVm&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=2
###  작성일 : 24-11-14
import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    box = list(0 for _ in range(N))

    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            box[j] = i

    print(f"#{tc}", *box)
