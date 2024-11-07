###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=30&pageIndex=1
###  참고한 내용 : https://velog.io/@seungjae/SWEA-1244.-SW-%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0-%EC%9D%91%EC%9A%A9-2%EC%9D%BC%EC%B0%A8-%EC%B5%9C%EB%8C%80-%EC%83%81%EA%B8%88-Python-%EC%99%84%EC%A0%84%ED%83%90%EC%83%89
###  작성일 : 24-11-07
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start = len(arr) // 2
    end = len(arr) // 2
    distance = "down"
    answer = 0
    for i in range(len(arr)):
        if start == 0:
            distance = "up"

        for j in range(len(arr)):
            if start <= j <= end:
                answer += arr[i][j]

        if distance == "up":
            start, end = start+1, end-1
        else:
            start, end = start-1, end+1

    print(f"#{tc}", answer)