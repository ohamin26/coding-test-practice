###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AW9j74FacD0DFAUY&categoryId=AW9j74FacD0DFAUY&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=2
###  작성일 : 24-11-14
import sys
from collections import deque

sys.stdin = open("input.txt")

T = int(input())


def parking(value):
    global income
    for i in range(n):
        if income[i] == 0:
            income[i] = value
            break


for tc in range(1, T + 1):
    n, m = map(int, input().split())
    R = list(int(input()) for _ in range(n))
    W = list(int(input()) for _ in range(m))
    income = [0 for _ in range(n)]
    wait = deque()
    cost = 0
    car = deque(int(input()) for _ in range(m * 2))
    while True:
        if len(wait) > 0:
            if 0 in income:
                parking(wait.popleft())
                continue
        if car[0] > 0:
            if not 0 in income:
                wait.append(car.popleft())
            else:
                parking(car.popleft())
        else:
            if abs(car[0]) in income:
                cur = car.popleft()
                idx = income.index(abs(cur))
                weight = R[idx]
                income[idx] = 0
                cost += W[abs(cur) - 1] * weight
        if len(car) == 0 and len(wait) == 0:
            break
    print(f"#{tc} {cost}")
