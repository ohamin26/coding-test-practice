###  문제 : https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
###  작성일 : 24-11-12
import sys

sys.stdin = open("input.txt")

T = int(input())


def move(arr, idx):
    if arr[idx][3] == 1:
        arr[idx][0] -= 1
    elif arr[idx][3] == 2:
        arr[idx][0] += 1
    elif arr[idx][3] == 3:
        arr[idx][1] -= 1
    elif arr[idx][3] == 4:
        arr[idx][1] += 1


def color(arr, idx):
    if arr[idx][0] == 0 or arr[idx][1] == 0 or arr[idx][0] == n - 1 or arr[idx][1] == n - 1:
        arr[idx][2] = int(arr[idx][2] / 2)
        if arr[idx][3] == 1:
            arr[idx][3] = 2
        elif arr[idx][3] == 2:
            arr[idx][3] = 1
        elif arr[idx][3] == 3:
            arr[idx][3] = 4
        elif arr[idx][3] == 4:
            arr[idx][3] = 3


def check(arr):
    for i in range(k):
        maxV = arr[i][2]
        maxT = arr[i][3]
        ssum = arr[i][2]
        for j in range(i + 1, k):
            if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1]:
                if maxV < arr[j][2]:
                    ssum += arr[j][2]
                    maxV = arr[j][2]
                    maxT = arr[j][3]
                    arr[j][2] = 0
                    arr[j][3] = 0
                else:
                    ssum += arr[j][2]
                    arr[j][2] = 0
                    arr[j][3] = 0
        arr[i][2] = ssum
        arr[i][3] = maxT


for tc in range(T):
    n, m, k = map(int, input().split())
    arr = [[0] * 4 for i in range(k)]
    for i in range(k):
        arr[i] = list(map(int, input().split()))
    while m > 0:
        for i in range(k):
            move(arr, i)
            color(arr, i)
        check(arr)
        m -= 1

    res = 0
    for i in range(len(arr)):
        res += arr[i][2]
    print("#{} {}".format(tc + 1, res))
