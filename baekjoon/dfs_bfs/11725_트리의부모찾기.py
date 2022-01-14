# # N = int(input())

# # graph = [[] for _ in range(N+1)]
# # graph = [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]
# # graph = {i:[] for i in range(N+1)}
# graph = {0: [], 1: [6, 4], 2: [4], 3: [6, 5], 4: [1, 2, 7], 5: [3], 6: [1, 3], 7: [4]}

# # for i in range(N-1):
# #     a,b = map(int, input().split())
# #     graph[a].append(b)
# #     graph[b].append(a)
# N=7

# for i in range(2, N+1):
#     for j in graph:
#         if i in graph[j]:
#             print('i, j:', i,j)


#dfs를 리스트로 만들어서 바로 전의 원소를 출력하면 되지 않나?
#4의 경우 5가 나옴... 허허..
# dfs_list = []
# def dfs(a):
#     visited[a] = True
#     dfs_list.append(a)
    
#     for i in graph[a]:
#         if not visited[i]:
#             dfs(i)



# # N = int(input())

# # graph = [[] for _ in range(N+1)]
# N = 7
# graph = [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]
# visited = [False for _ in range(N+1)]

# for i in range(N-1):
#     a,b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)


#역시나 답지를 보게 된 나.. 슬프네요.. 
import sys
sys.setrecursionlimit(10**6) #이거 안해주면 오류남
input = sys.stdin.readline #이거 안해주면 시간이 진짜 느림
def dfs(s, graph, parents):
    for i in graph[s]: 
        if parents[i] == 0: 
            parents[i] = s 
            dfs(i, graph, parents) 

N = int(input())
graph = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]


for i in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph) #[[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

dfs(1,graph, parents) #parents 만들기
for i in range(2,len(parents)):
    print(parents[i])




        

    