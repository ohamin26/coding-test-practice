###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV5LyE7KD2ADFAXc&categoryId=AV5LyE7KD2ADFAXc&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  작성일 : 24-11-11
import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    puzzle = [list(input()) for _ in range(H)]
    N = int(input())
    cmd = input()

    cur = [0, 0]
    for i in range(H):
        for j in range(W):
            if puzzle[i][j] in "^v<>":
                cur = [i, j]

    for st in cmd:
        if st == "S":
            if puzzle[cur[0]][cur[1]] == "^":
                for i in range(cur[0] - 1, -1, -1):
                    if puzzle[i][cur[1]] == "*":
                        puzzle[i][cur[1]] = "."
                        break
                    elif puzzle[i][cur[1]] == "#":
                        break
            elif puzzle[cur[0]][cur[1]] == "v":
                for i in range(cur[0] + 1, H):
                    if puzzle[i][cur[1]] == "*":
                        puzzle[i][cur[1]] = "."
                        break
                    elif puzzle[i][cur[1]] == "#":
                        break
            elif puzzle[cur[0]][cur[1]] == ">":
                for i in range(cur[1] + 1, W):
                    if puzzle[cur[0]][i] == "*":
                        puzzle[cur[0]][i] = "."
                        break
                    elif puzzle[cur[0]][i] == "#":
                        break
            elif puzzle[cur[0]][cur[1]] == "<":
                for i in range(cur[1] - 1, -1, -1):
                    if puzzle[cur[0]][i] == "*":
                        puzzle[cur[0]][i] = "."
                        break
                    elif puzzle[cur[0]][i] == "#":
                        break
        else:
            new_row, new_col = cur
            direction = puzzle[cur[0]][cur[1]]
            if st == "U":
                new_row, new_col, direction = cur[0] - 1, cur[1], "^"
            elif st == "D":
                new_row, new_col, direction = cur[0] + 1, cur[1], "v"
            elif st == "L":
                new_row, new_col, direction = cur[0], cur[1] - 1, "<"
            elif st == "R":
                new_row, new_col, direction = cur[0], cur[1] + 1, ">"

            if 0 <= new_row < H and 0 <= new_col < W and puzzle[new_row][new_col] == ".":
                puzzle[cur[0]][cur[1]] = "."
                cur = [new_row, new_col]
            puzzle[cur[0]][cur[1]] = direction

    print(f"#{tc}", end=" ")
    for row in puzzle:
        print("".join(row))
