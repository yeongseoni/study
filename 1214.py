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
stack=[]
stack.append(1)
stack.append(2)
stack.append(5)
stack.append(6)
stack.pop()
stack.append(7)
print(stack) #최하단 원소부터 출력
print(stack[::-1]) #최상단 원소부터 출력

#큐란? 먼저 들어온 데이터가 먼저 나가는 형식(선입선출), 입구와 출구가 모두 뚫려있는 터널과 같은 형태
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력
queue.reverse()
print(queue) #나중에 들어온 순서대로 출력
print("="*100)
print()

#프로그래머스 큰 수 만들기 남의 풀이
#문제의 정의가 혼동이 있는듯, 주어진 문자열 기본으로 해서 제일 큰 수를 만든다고 생각하면 될듯
#k=pop한 숫자다
def solution(number, k):
    stack=[number[0]]
    for num in number[1:]:
        print('num:',num,k,stack)
        while len(stack)>0 and stack[-1] < num and k>0:
            k-=1
            stack.pop()
        print('num, k, stack:',num,k, stack)
        stack.append(num)
    if k!=0: #왜 해주는 걸까? 
        stack = stack[:-k]
    return ''.join(stack)
solution('1231234',3)