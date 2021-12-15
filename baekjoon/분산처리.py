#처음 풀이 -> 시간초과
# n = int(input())
# for i in range(n):
#     a,b = map(int, input().split())
#     answer  = (a ** b) % 10
#     print(answer)


#2번째 풀이->시간초과
# n = int(input())
# for i in range(n):
#     a,b = map(int, input().split())
#     what  =  a ** b
#     what = list(str(what))
#     what2 = int(what[-1])
#     answer  = what2 % 10
#     print(answer)


#3번째 풀이
# n = int(input())
# for i in range(n):
#     a,b = map(int, input().split())
#     what  =  list(str(a ** b))
#     what2 = int(what[-1])
#     answer  = what2 % 10
#     if answer == 0:
#         answer = 10
#     print(answer)

#4번째 풀이
#계속 시간 초과가 떠서 질문을 활용
#pow = 제곱근 구해주는 함수, pow(a,b,c) 해줄 경우 a**b%c
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    answer  =  pow(a,b,10)
    if answer == 0:
        answer = 10
    print(answer)

    #이렇게도 가능
    #if answer: print(answer)
    #else: print(10)

