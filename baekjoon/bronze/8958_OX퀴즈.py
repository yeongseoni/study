import sys
input = sys.stdin.readline


N = int(input())
quiz = [[input()] for _ in range(N)]


for i in quiz:

    num = [0 for _ in range(len(i[0]))]
    
    #첫 문자에 해당하는 값 넣어주기
    if i[0][0] == 'O':
        num[0] = 1
    else:
        num[0] = 0
        
    for j in range(1,len(i[0])):
        if i[0][j] == 'O':
            num[j] = num[j-1] + 1
        else:
            num[j] = 0
            
    print(sum(num))


#남의 코드
#이게 더 간단할듯

#처음 횟수 받고
a = int(input())
for i in range(a):
    #횟수만큼 문자열 받음
    b = input()
    #리스트화 시켜서 각 원소 하나하나 리스트 들어가게
    s = list(b)
    sum = 0
    c = 1
    for i in s:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)
