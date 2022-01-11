from collections import deque

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or nx>=3 or ny<0 or ny>=3: #벗어나는 경우 처리
                continue
            if graph[nx][ny] == 0: #이미 방문경우 처리
                continue
            if graph[nx][ny] == 1: #한 번도 방문하지 않았을때 처리
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
            
    return graph[2][2]
            
graph = [[1,1,0],
         [0,1,0],
         [0,1,1]]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))
    