#bfs를 사용해야하는게 아닐까?

n,m = 4,3
graph = [[], [3], [3,4], [1,2], [2]]
visited = [False for _ in range(n+1)]


def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            print('i', i)
            dfs(graph, i, visited)

cnt=0
for i in range(1,n+1):
    if not visited[i]:
        cnt+=1
        dfs(graph, i, visited)
print(cnt)