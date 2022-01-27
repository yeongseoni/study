#분할해서 구현하려는 아이디어 - 실패
#이 문제 이해를 못하겠음
#N=9
paper= [[0,0,0,1,1,1,-1,-1,-1],
         [0,0,0,1,1,1,-1,-1,-1],
         [0,0,0,1,1,1,-1,-1,-1],
         [1,1,1,0,0,0,0,0,0],
         [1,1,1,0,0,0,0,0,0],
         [1,1,1,0,0,0,0,0,0],
         [0,1,-1,0,1,-1,0,1,-1],
         [0,-1,1,0,1,-1,0,1,-1],
         [0,1,-1,1,0,-1,0,1,-1]]

# cnt = {0:0, 1:0, -1:0}

# N=4
# test = [[0,0,0,1],
#         [0,0,0,1],
#         [0,0,0,1],
#         [0,0,0,1]]

# def check(x,y,test):
#     a = []
#     for i in range(3):
#         for j in range(3):
#             if x+i >-1 and x+i <N and y+i >-1 and y+i<N:
#                 a.append(test[x+i][y+j])
#     if sum(a) == 0:
#         cnt[0] +=1
#     elif sum(a) == 9:
#         cnt[1] +=1
#     elif sum(a) == -9:
#         cnt[-1] +=1
#     else:
#         pass

# for i in range(0,N+1,3):
#     for j in range(0,N+1,3):
#         print(i,j)
#         check(i,j,test)
# print(cnt)


import sys
read = sys.stdin.readline
# n = int(read())
n=9
# paper = [ list(map(int, read().split())) for _ in range(n) ]

result_min, result_zero, result_plus = 0 , 0 , 0

def cut(x,y,n):
    global result_min, result_zero , result_plus 
    check = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != paper[i][j]: # 9등분하기 
                for a in range(3):
                    for b in range(3):
                        cut( x + n//3*a, y + n//3*b, n//3 )
                return
    if check == -1 :
        result_min += 1
    elif check == 0 :
        result_zero += 1
    elif check == 1 :
        result_plus += 1 

cut(0,0,n)
print(result_min)
print(result_zero)
print(result_plus)