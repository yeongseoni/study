from collections import deque

def bfs(a,b):
    queue = deque()
    queue.append([a,b])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                queue.append([nx,ny])
    print(graph[n-1][m-1]) 
    

n,m = map(int, input().split())
#한줄에 띄어쓰기 없이 정수 여러개 받았을때, 2차원 배열로 저장 ->몰랐음
graph = [list(map(int, input())) for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

bfs(0,0)


