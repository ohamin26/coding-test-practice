###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-07
for tc in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.append(list([0] * N))
    answer = 0
    for i in range(N):
        check = 0
        for j in range(N):
            if arr[j][i] == 1:
                check = 1
            elif arr[j][i] == 2:
                if check == 1:
                    answer += 1
                check = 0
    print(f"#{tc}",answer)