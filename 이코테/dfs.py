import sys
sys.setrecursionlimit(10**6)
#dfs 기본코드
def dfs(v):
    visited[v] = 0  #잊지말자 방문처리
    print(v, end='')
    for i in graph[v]:
        if visited[i] == 1:
            dfs(i)


graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7,8],[2,6,8],[7]]
visited = [1 for _ in range(9)]

# dfs(1)

#bfs
from collections import deque

def bfs(a):
    queue = deque()
    queue.append(a)
    visited[a] = 0  #가장 처음 방문 노드 처리
    while queue:
        start = queue.popleft()
        print(start, end='')
        
        for i in graph[start]:
            if visited[i]==1:
                queue.append(i) #원소 넣어주고
                visited[i] = 0 #넣어줬으니 방문처리



graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7,8],[2,6,8],[7]]
visited = [1 for _ in range(9)]

#bfs(1)


#음료수 얼려먹기, 또 틀림... 
def drink_dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M: #먼저 주어진 범위를 벗어나면 즉시 종료한다
        return False
    if drink_graph[x][y] == 0:
        drink_graph[x][y] = 1
        
        drink_dfs(x-1, y)
        drink_dfs(x, y-1)
        drink_dfs(x+1, y)
        drink_dfs(x,y+1)
        return True
        # for i in range(4):
        #     nx = x + dx[i]
        #     ny = y + dy[i]
        #     drink_dfs(nx, ny)
            
    return False



N,M = 4,5 #세로, 가로
drink_graph = [[0,0,1,1,0],
         [0,0,0,1,1],
         [1,1,1,1,1],
         [0,0,0,0,0]]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
for i in range(N):
    for j in range(M):
        if drink_dfs(i,j) == True:
            cnt+=1

#print(cnt)


#미로탈출 -> 풀긴 풀었따..?
def miro_bfs(a,b):
    queue2 = deque()
    queue2.append([a,b])
    
    while queue2:
        x,y = queue2.popleft()
        for i in range(4): #현재 위치에서 4가지 방향 확인
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: #미로 벗어나면 무시
                continue
            if miro[nx][ny] == 1: #해당 노드 처음 방문하는 경우에만 최단 거리 기록
                miro[nx][ny] += miro[x][y]
                queue2.append([nx,ny])  #난 이걸 위로 올렸는데...
        
    


n,m = 5,6
miro = [[1,0,1,0,1,0],
        [1,1,1,1,1,1],
        [0,0,0,0,0,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1]]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

miro_bfs(0,0)
print(miro[n-1][m-1])