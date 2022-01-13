# #구현 실패,, 왜 인덱스 에러가 날까?
# def dfs(test2, a, visited):
#     visited[a] = True
    
#     for i in test2[a]:
#         if not visited[i]:
#             dfs(test2, i, visited)
#     print(test2)


# test = [['A','B','C'], ['B','D', '.']]

# #내가 생각한 아이디어:어차피 행의 첫번째 원소는 부모노드이니까 그걸 따로 빼서 리스트에 넣으려고 함
# #A=1 , B=2 이런식 하려했는데 만약에 A~Z나왔을때 일반화가 안돼... ->ord 이용하면 1부터 가능

# test2 = [[]] #전체 리스트 만들기
# for i in range(len(test)):
#     test3 = [] #2차원 리스트 만들기, 실제 원소 들어갈 부분
#     for j in range(1,len(test[i])):
#         if test[i][j] == '.':
#             continue
#         else:
#             test3.append(ord(test[i][j])-64)
#     test2.append(test3)
# print(test2)

# visited = [False for _ in range(5)]


# dfs(test2, 1, visited)
    
#결국 답안을 보고 이해하기로 함
#딕셔너리를 사용하는게 꽤나 괜찮은듯?

def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])
    
def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')


N = int(input())
tree = {}
for i in range(N):
    node, left, right = input().split()
    tree[node] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')

    

