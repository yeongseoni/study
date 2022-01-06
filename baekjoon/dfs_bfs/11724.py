# from collections import deque
# import sys
# sys.setrecursionlimit(10000)
# n,m = map(int, sys.stdin.readlines().split())
# graph = [[] for _ in range(n+1)]

# # n,m = int(input().split())
# n,m=6,5
# # graph = [[] for _ in range(n+1)]
# # print(graph)

# # for i in range(m):
# #     a,b = map(int, input().split())
# #     graph[a].append(b)
# #     graph[b].append(a)
# # print(graph)
# # for i in graph:
# #     i.sort()


# graph = [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
# visited = [False for _ in range(n+1)]


# def dfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 print('check i', i)
#                 dfs(graph, i, visited)
            
# cnt=0
# for i in range(1,n+1):
#     if not visited[i]:
#         cnt+=1
#         dfs(graph, i, visited)

# print(cnt)




# from collections import deque
# import sys

# def dfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 dfs(graph, i, visited)

# n,m = map(int, sys.stdin.readlines().split())
# graph = [[] for _ in range(n+1)]
# visited = [False for _ in range(n+1)]

# for i in range(m):
#     a,b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# for i in graph:
#     i.sort()
    
                
# cnt=0
# for i in range(1,n+1):
#     if not visited[i]:
#         cnt+=1
#         dfs(graph, i, visited)

# print(cnt)
a=1
print(a)