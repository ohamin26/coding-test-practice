###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do
###  작성일 : 24-11-19
for tc in range(10):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(100))
    maxNum = 0
    for i in range(len(arr)) :
        sumX = 0
        sumY = 0
        for j in range(len(arr)) :
            sumX += arr[i][j]
            sumY += arr[j][i]
        maxNum = max(sumX, sumY, maxNum)

    sumZL = 0
    sumZR = 0
    for i in range(0,100):
        sumZL += arr[i][i]
        sumZR += arr[99-i][i]

    maxNum = max(sumZL, sumZR, maxNum)

    print(f"#{tc+1}",maxNum)