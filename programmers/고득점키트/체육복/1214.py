#프로그래머스 체육복 문제 내 풀이
def solution(n, lost, reserve):
    std = [0 for i in range(n) if str(i+1) in lost -1]
    
    for i in lost:
        std[i-1] -=1
    for i in reserve:
        std[i-1] +=1
        
    for i in range(n):
        if std[i] <0 and std[i+1]>=1:
            std[i] +=1
            std[i+1]-=1
    cnt = 0
    for i in std:
        if i >=0:
            cnt+=1
    return cnt

#프로그래머스 체육복 문제 남의 풀이
#set 하면 알아서 정렬도 해준다.. sort 자동
