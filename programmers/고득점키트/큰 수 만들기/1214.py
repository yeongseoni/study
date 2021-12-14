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
        while len(stack)>0 and stack[-1] < num and k>0:
            k-=1
            stack.pop()
        stack.append(num)
    if k!=0: #왜 해주는 걸까? 
        stack = stack[:-k]
    return ''.join(stack)


