#bfs가 아닐까? -> 응 아님

# from collections import deque

# N,M = 2,4


# graph = []
# for i in range(N):
#     graph.append([0 for _ in range(M)])

    

# #가장 왼쪽 아래의 경우 N-1, 0

# def bfs(x,y):
#     graph[x][y] = 1
#     queue = deque()
#     queue.append([x,y])
#     while queue:
#         x,y = queue.popleft()
        
#         dx = [-2, -1, 1, 2]
#         dy = [1, 2, 2, 1]
#         for _ in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx<0 or nx >N or ny <0 or ny >M:
#                 continue
#             if graph[nx][ny] == 1:
#                 continue
#             if graph[nx][ny] != 1:
#                 graph[nx][ny] = 1
#                 queue.append([nx,ny])

# bfs(N-1,0)
# print(f'graph:{graph}')




#답지 아이디어를 보고 하기로 함->못함
#문제 이해를 못하겠는데?
#가로랑 세로 의미도 ???? 헷갈리는데???
#이해 못하겠다 .. ^^... 어느 조건을 빠뜨린 걸까
#n번 틀린듯 이제 짜증나서 일단 넘어감

N,M = list(map(int,input().split()))

if M==1:
    cnt=1
elif N==2:
    if M <7:
        cnt=M//2
    else:
        cnt=4
else:
    if M<5:
        cnt=M
    elif M<7:
        cnt=4
    else:
        cnt=M-2
print(cnt)