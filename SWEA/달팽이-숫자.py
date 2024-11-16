###  문제 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq
###  작성일 : 24-11-17
T = int(input())

dr = [0,1,0,-1]
dc = [1,0,-1,0]

for tc in range(1,T+1) :
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    r,c = 0,0
    dist = 0
    
    for n in range(1, N*N+1) :
        snail[r][c] = n
        r += dr[dist]
        c += dc[dist]
        
        if r < 0 or c < 0 or r >= N or c >= N or snail[r][c] != 0 :
            r -= dr[dist]
            c -= dc[dist]
            
            dist = (dist + 1) % 4
            
            r += dr[dist]
            c += dc[dist]
            
    print(f"#{tc}")
    for row in snail :
        print(" ".join(map(str, row)))
