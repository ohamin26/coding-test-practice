###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV19AcoKI9sCFAZN&categoryId=AV19AcoKI9sCFAZN&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-07
import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = input()
    bit = [0 for _ in range(len(N))]
    answer = 0
    for i in range(len(N)):
        if not bit[i] == int(N[i]):
            answer += 1
            for j in range(i, len(N)):
                bit[j] = int(N[i])
        st = ""
        for z in bit:
            st += str(z)
        if st == N:
            break
    print(f"#{tc}",answer)