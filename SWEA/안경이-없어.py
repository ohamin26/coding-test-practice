###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWl0ZQ8qn7UDFAXz&categoryId=AWl0ZQ8qn7UDFAXz&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=2
###  작성일 : 24-11-15
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    A, B = map(str,input().split())
    one_hole = ["A", "D", "O", "P", "Q", "R"]
    state = "SAME"
    if len(A) != len(B):
        state = "DIFF"
    else:
        for i in range(len(A)):
            if A[i] == B[i] == "B":
                continue
            if A[i] in one_hole:
                if not B[i] in one_hole:
                    state = "DIFF"
                    break
            if B[i] in one_hole:
                if not A[i] in one_hole:
                    state = "DIFF"
                    break
    print(f"#{tc} {state}")