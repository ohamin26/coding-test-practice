###  https://school.programmers.co.kr/learn/courses/30/lessons/42895?language=python3
###  solution만 작성
###  참고한 내용 : https://www.youtube.com/watch?v=ZsVVTEfZee8
###  작성일 : 24-11-04
###
def solution(N, number):
    if N == number:
        return 1
    
    answer = -1
    arr = [set() for _ in range(8)]
    
    for i in range(len(arr)):
        arr[i].add(int(str(N)*(i+1)))
    
    for i in range(1,8):
        for j in range(i):
            for op1 in arr[j]:
                for op2 in arr[i-j-1]:
                    arr[i].add(op1+op2)
                    arr[i].add(op1-op2)
                    arr[i].add(op1*op2)
                    if op2 != 0:
                        arr[i].add(op1//op2)
        if number in arr[i]:
            answer = i+1
            break
    print(arr)
    return answer