###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWGsRbk6AQIDFAVW&categoryId=AWGsRbk6AQIDFAVW&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-14
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    card = list(map(str, input().split()))
    half = N // 2
    if len(card) % 2 == 1:
        half += 1
    A = card[0:half]
    B = card[half:]
    newCard = []
    for i in range(half):
        if len(B) == i:
            break
        newCard.append(A[i])
        newCard.append(B[i])
    if len(newCard) != len(card):
        newCard.append(A[-1])
    print(f"#{tc}",*newCard)