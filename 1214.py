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



#프로그래머스 큰 수 만들기
from itertools import combinations
def solution(number, k):
    make_c = list(combinations(number, len(number)-k))
    num_list = []
    for i in make_c:
        str = ''.join(i)
        num_list.append(str)
    
    num_set = set(num_list)
    
    return (max(num_set))

#해당 문제 풀이 위해 스택 이용함
#스택이란? 먼저 들어온 데이터가 나중에 나가는 형식, 파이썬에서는 리스트로(append, pop)구현
#입구와 출구가 동일한 형태
print('hello')