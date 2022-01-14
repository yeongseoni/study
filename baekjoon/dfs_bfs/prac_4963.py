#실패
import sys
sys.setrecursionlimit(10**6)


def dfs(x,y,graph):
    if not(x<0 or x>=w or y<0 or y>=h):
        if graph[x][y] == 1:
            graph[x][y] = 0
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if graph[nx][ny] == 0:
                continue
            else:
                dfs(nx, ny, graph)
    
    
# h,w = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(h)]
# print(graph)
# # h,w = 3,2
# # graph = [[1,1,1], [1,1,1]]

# dx = [-1,1,0,0,-1,-1,1,1]
# dy = [0,0,-1,1,-1,1,-1,1]

# cnt=0
# for i in range(w):
#     for j in range(h):
#         if graph[i][j] == 1:
#             cnt+=1
#             dfs(i, j)
        
# print(cnt)

while True:
    h,w = list(map(int, input().split()))
    graph = [list(map(int, input().split())) for _ in range(w)]
    if h==0 and w==0:
        break
    
    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]
    
    cnt=0
    for i in range(w):
        for j in range(h):
            if graph[i][j] == 1:
                dfs(i, j, graph)
                cnt+=1
                

    print(cnt)