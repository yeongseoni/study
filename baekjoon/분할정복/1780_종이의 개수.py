#분할해서 구현하려는 아이디어 - 실패
#이 문제 이해를 못하겠음
#N=9
graph = [[0,0,0,1,1,1,-1,-1,-1],
         [0,0,0,1,1,1,-1,-1,-1],
         [0,0,0,1,1,1,-1,-1,-1],
         [1,1,1,0,0,0,0,0,0],
         [1,1,1,0,0,0,0,0,0],
         [1,1,1,0,0,0,0,0,0],
         [0,1,-1,0,1,-1,0,1,-1],
         [0,-1,1,0,1,-1,0,1,-1],
         [0,1,-1,1,0,-1,0,1,-1]]

cnt = {0:0, 1:0, -1:0}

N=4
test = [[0,0,0,1],
        [0,0,0,1],
        [0,0,0,1],
        [0,0,0,1]]

def check(x,y,test):
    a = []
    for i in range(3):
        for j in range(3):
            if x+i >-1 and x+i <N and y+i >-1 and y+i<N:
                a.append(test[x+i][y+j])
    if sum(a) == 0:
        cnt[0] +=1
    elif sum(a) == 9:
        cnt[1] +=1
    elif sum(a) == -9:
        cnt[-1] +=1
    else:
        pass

for i in range(0,N+1,3):
    for j in range(0,N+1,3):
        print(i,j)
        check(i,j,test)
print(cnt)


