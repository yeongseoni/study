#하노이의 탑은 n-1의 숫자들을 2로 옮기고 1을 3자리에 옮긴 후 다 옮기면 끝
#잔꾀는 역시 안되나보다
#내가 완전 잘못 생각함 왜그랬지??????
#4321 순으로 깔려있음!!!!
# from collections import deque
# import sys
# input = sys.stdin.readline

# #K = 3
# K = int(input())


# one = deque([i for i in range(K,0,-1)])
# two = deque()
# three = deque()
# print(one)

# for i in range(K-1):
#     two.append(one.popleft())
#     print(1,2)
    
# three.append(one.popleft())
# print(1,3)

# for i in range(K-1):
#     three.append(two.popleft())
#     print(2,3)
#     print(three)
    
#남의 답
#이거 이해도 어렵다...

def hanoi(N, a, c, b): #원반개수, 시작, 목표, 보조
    if N == 1:
        print('one',a, c)
        return
    hanoi(N-1, a, b, c) #마지막 가장 큰 원판을 제외하고는 목표기둥이 아닌 보조기둥으로 가야하기 떄문
    print(a, c) #n-1개 다 옮기고 마지막 큰 원판 옮기는 거임
    hanoi(N-1, b, c, a)
    
hanoi(3,1,3,2)