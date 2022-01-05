from collections import deque

#dfs, bfs의 기초라고 볼 수 있음(이코테 금방 까먹었음)
def dfs(graph, s, visited):
    print(s, end = ' ')
    visited[s] = True
    for i in graph[s]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, s, visited):
    queue = deque([s])
    visited[s] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



n,m,start = map(int, input().split())

graph = [[] for _ in range(n+1)]
#graph[b].append(a)를 해주지 않으면 3,4 일때 4에는 빈 리스트...
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
#sort를 해줘서 2부터 방문하게 해줌, 이거 안해주면 3부터 방문한다
for i in graph:
    i.sort()

#for문 쓰지않고 그냥 False * (n+1)하면 [0] 나옴
visited = [False for _ in range(n+1)]
visited2 = [False for _ in range(n+1)]

dfs(graph, start, visited)
print()
bfs(graph, start, visited2)
