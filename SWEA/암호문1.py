###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14w-rKAHACFAYD&categoryId=AV14w-rKAHACFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-11
import sys

sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    origin = list(map(str, input().split()))
    C = int(input())
    command = input().split("I ")[1:]
    for st in command:
        arr = st.split()
        cnt = int(arr[0])
        length = int(arr[1])
        change = arr[2:2+length]
        for i, value in enumerate(change):
            origin.insert(cnt+i, value)

    print(f"#{tc}",*origin[0:10])