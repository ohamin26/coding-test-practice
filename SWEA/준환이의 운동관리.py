###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWE_ZXcqAAMDFAV2&categoryId=AWE_ZXcqAAMDFAV2&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-14
T = int(input())

for tc in range(1, T + 1):
    L, U, X = map(int, input().split())
    time = 0
    if X < L:
        time = L - X
    elif X > U:
        time = -1

    print(f"#{tc} {time}")