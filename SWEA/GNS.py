###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14jJh6ACYCFAYD&categoryId=AV14jJh6ACYCFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-14
import sys
sys.stdin = open("input.txt")

T = int(input())


def find(n):
    global number
    for k, v in enumerate(number):
        if k == n:
            print(v, end=" ")


for tc in range(1, T + 1):
    C, N = map(str, input().split())
    arr = list(map(str, input().split()))
    number = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR": 4, "FIV" : 5, "SIX" : 6, "SVN": 7, "EGT": 8, "NIN": 9}
    answer = []
    for i in arr:
        answer.append(number[i])
    answer.sort()
    print(f"#{tc}")
    for i in answer:
        find(i)