###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14Rq5aABUCFAYi&categoryId=AV14Rq5aABUCFAYi&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-11
import sys

sys.stdin = open("input.txt", "r")


def check(arr):
    start = ""
    end = ""
    for i in range(len(arr)):
        start += arr[i]
        end += arr[len(arr) - i - 1]
        if not start == end:
            return 0
    return len(start)


for tc in range(1,11):
    N = int(input())
    puzzle = [list(map(str, input())) for _ in range(100)]
    puzzleL = list(map(list, zip(*puzzle)))
    maxL = 0
    for i in range(100):
        cur = puzzle[i]
        cur2 = puzzleL[i]
        for j in range(100):
            for z in range(1, 101):
                curL = check(cur[j:z])
                curR = check(cur2[j:z])
                maxL = max(curL, curR, maxL)
    print(f"#{tc}",maxL)