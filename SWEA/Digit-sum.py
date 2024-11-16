###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWHPiSYKAD0DFAUn&categoryId=AWHPiSYKAD0DFAUn&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=2
###  작성일 : 24-11-15
import sys

sys.stdin = open("input.txt")

T = int(input())

result = []

for tc in range(1, T + 1):
    n = input()
    num = n
    while len(n) > 1:
        num = sum(map(int, n))
        n = str(num)
    result.append(num)
for idx, value in enumerate(result):
    print('#%d %s' % (idx + 1, value))
