import sys
sys.setrecursionlimit(10**6)

def dfs(graph, a, b):
    graph[a][b] = 0 #방문처리

    for i in range(8):
        nx = a + dx[i]
        ny = b + dy[i]
        
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:
            dfs(graph, nx,ny)

        
    

while True:
    m,n = map(int,input().split())
    if m==0 and n==0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == True:
                cnt+=1
                dfs(graph,i,j)

    print(cnt)