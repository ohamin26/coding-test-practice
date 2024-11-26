###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do
###  작성일 : 24-11-26
def shift(arr):
    first = arr[0]
    for i in range(len(arr)):
        if i == len(arr)-1:
            arr[i] = first
        else:
            arr[i] = arr[i+1]


for tc in range(1, 11):
    N = int(input())
    numArr = list(map(int, input().split()))
    cnt = 1
    while not numArr[len(numArr) - 1] == 0:
        num = numArr[0]
        num -= cnt
        if num > 0:
            shift(numArr)
            numArr[len(numArr) - 1] = num
            cnt += 1
        else:
            shift(numArr)
            numArr[len(numArr) - 1] = 0
            break
        if cnt > 5:
            cnt = 1
    print(f"#{tc}", *numArr)