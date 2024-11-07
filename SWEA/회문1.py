###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14QpAaAAwCFAYi&categoryId=AV14QpAaAAwCFAYi&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-07
def check(st):
    global answer
    first = ""
    end = ""
    for i in st:
        first += str(i)
    for j in range(len(st), 0, -1):
        end += str(st[j - 1])
    if first == end:
        answer += 1


for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(8)]
    answer = 0
    arr2 = []
    for i in range(8):
        st = ""
        for j in range(8):
            st += arr[j][i]
        arr2.append(st)
    for st in range(8):
        for i in range(0, 8-N+1):
            check(arr[st][i:i + N])
            check(arr2[st][i:i + N])

    print(f"#{tc}", answer)