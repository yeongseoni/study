#첫번째 시도, 테스트 케이스 맞는데 답이 틀리다고 함 -> 근데 왜인지는 모름..?
# def dfs(arr, s, visited):
#     visited[s] = True
#     for i in check[s]:
#         if not visited[i]:
#             dfs(arr, i, visited)


# T = int(input())
# for i in range(T):
#     N = int(input())
#     ip = list(map(int, input().split()))
#     arr = [i for i in range(1,N+1)]
#     check = [[] for i in range(N+1)]
#     visited = [False for i in range(N+1)]
    
#     #행렬 만들기
#     for i in range(N):
#         check[i+1].append(ip[i])
#         check[ip[i]].append(arr[i])
#     #정렬   
#     for i in check:
#         i.sort()

    
#     cnt = 0
#틀린 이유 밑에 for문에 범위 N+1까지였어야함 
#조금 당황스럽다
#     for i in range(1,N):
#         if not visited[i]:
#             cnt += 1
#             dfs(arr, i, visited)
#     print(cnt)

#두 번째 시도, 다른 사람의 코드 보고 좀 변경해보기로 함
def dfs(s, visited):
    visited[s] = True
    for i in check[s]:
        if not visited[i]:
            dfs(i, visited)
            
T = int(input())
for i in range(T):
    N = int(input())
    nodes = list(map(int, input().split()))
    
    check = [[] for i in range(N+1)]
    visited = [False for i in range(N+1)]
    
    #행렬 만들기
    for i in range(1,N+1):
        check[i].append(nodes[i-1])
        check[nodes[i-1]].append(i)
    #정렬   
    for i in check:
        i.sort()

    
    cnt = 0     
    for i in range(1,N+1):
        if not visited[i]:
            cnt += 1
            dfs(i, visited)
    print(cnt)