#재귀함수:자기 자신을 다시 호출하는 함수
#스택을 사용해야 할 때 스택 라이브러리 대신에 재귀함수를 이용하는 경우가 많다

# def recursive_function():
#     print("재귀함수를 호출합니다")
#     recursive_function()

    
# recursive_function()


#종료조건이 있는 재귀함수
#(1번째(2번째(3번쨰...(99번째(100번째))))) 이런식으로 호출되기 때문에 99번째 종료 - 98번째 종료 이렇게 나옴
# def recursive_function(i):
    
#     if i==100:
#         return
#     print(i,'번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
#     recursive_function(i+1)
#     print(i,'번째 재귀함수를 종료합니다.')

# recursive_function(1)

# #반복문 이용한 팩토리얼 구현

# def factorial_iterative(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result

# #재귀적으로 구현
# def factorial_recursive(n):
#     if n <= 1:
#         return 1
    
#     return n * factorial_recursive(n-1)

# print("반복으로 구현:",factorial_iterative(6))
# print("재귀로 구현:", factorial_recursive(6))

# def gcd(a,b):
#     if a%b == 0:
#         return b
#     else:
#         print(a,b)
#         return gcd(b, a%b)
# print(gcd(162, 192))

# print("="*100)
# #dfs : 깊이 우선 탐색, 깊은 부분을 우선적으로 탐색하는 알고리즘
# #스택 자료구조(혹은 재귀함수)를 이용
# #1.탐색 시작 노드 스택에 삽입하고 방문처리
# #2.스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드 스택에 넣고 방문처리, 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
# #3.더이상 2번의 과정을 수행할 수 없을때까지 반복

# def dfs(graph, v, visited):
#     #현재 노드를 방문 처리
#     visited[v] = True
#     print(v, end=' ')

#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
    
# #각 노드가 연결된 정보
# #0부터 시작해서 0은 빈 리스트, 1과 연결된거 2,3,8 이런 식
# graph = [[],[2,3,8],[1,7,8],[1,4,5],
#             [3,5],[3,4],[7],[2,6,8],[1,7]]
    
# visited = [False] * 9

# dfs(graph, 1, visited)

# print()
# print("="*100)
# print()
# #bfs : 너비 우선 탐색, 그래프에서 가장 가까운 노드부터 우선 탐색
# #큐 자료 구조 이용
# #1.탐색 시작 노드를 큐에 삽입하고 방문 처리
# #2.큐에서 노드 꺼낸 뒤에 해당 노드의 인접 노드 중 방문하지 않은 노드 모두 큐에 삽입하고 방문 처리
# #3.더이상 2번의 과정을 수행할 수 없을때까지 반복
# #최단 거리 문제로도 사용 가능

# from collections import deque

# def bfs(graph, start, visited):
#     queue = deque([start])

#     #현재 노드를 방문 처리
#     visited[start] = True

#     #큐가 빌때까지 반복
#     while queue:
#         v = queue.popleft()
#         print(v, end=" ")
#         #아직 방문하지 않은 인접한 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# graph = [[],[2,3,8],[1,7,8],[1,4,5],
#             [3,5],[3,4],[7],[2,6,8],[1,7]]
    
# visited = [False] * 9

# bfs(graph, 1, visited)

# print()
# print("="*100)
# print()
# print("음료수 얼려 먹기")

#음료수 얼려 먹기
#내코드

# graph = [[0,0,1,1,0], [0,0,0,1,1], [1,1,1,1,1], [0,0,0,0,0]]


# visit2 = []
# for i in range(4):
#     for j in range(5):
#         if graph[i][j] == 0:
#             x = (i*5)+j
#             visit1 = []
#             if 0<=i-1<4 and graph[i-1][j] == 0:
#                 visit1.append(x-5)
#             if 0<=j-1<5 and graph[i][j-1] == 0:
#                 visit1.append(x-1)
#             if 0<=j+1<5 and graph[i][j+1] == 0:
#                 visit1.append(x+1)
#             if 0<=i+1<4 and graph[i+1][j] == 0:
#                 visit1.append(x+5)
#             if not visit1:
#                 visit1.append(x)
#         else:
#             visit1 = []
#         visit2.append(visit1)
# print(visit2)

# visit3 = [False] * 19

# def water(visit2, v, visit3):
#     visit3[v] = True
#     print(v, end=" ")
    
#     for i in visit2[v]:
#         if not visit3[i]:
#             water(visit2, i, visit3)
    


# water(visit2, 5, visit3)

# visit=[]
# for i in range(20):
#     visit2 = []
#     if tot[i] == 0:
#         if 0<i-5<20 and tot[i-5]==0:
#             visit2.append(i-5)
#         if 0<i+5<20 and tot[i+5]==0:
#             visit2.append(i+5)
#         if 0<i+1<20 and tot[i+1]==0:
#             visit2.append(i+1)
#         if 0<i-1<20 and tot[i-1]==0:
#             visit2.append(i-1)
#         if not visit2:
#             visit2.append(i) #자기자신
#     else:
#         pass
#     visit.append(visit2)
# print(visit)

import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    if graph[x][y] == 0:
        graph[x][y] == 1

        dfs(x-1, y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result +=1
print(result)