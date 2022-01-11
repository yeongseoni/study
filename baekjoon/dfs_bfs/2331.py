# a = int(input())
# p = 2

# number = [a]

# s=0
# for i in list(str(a)):
#     s += int(i)**p
# number.append(s)
# print(number)

    
# funct(a,p)
# print()

# for i in range(1,100):
#     s=0
#     for i in list(str(a)):
#         s += int(i)**p
#     number.append(s)
# print(number)
    

# # test = []
# # sum=0
# # while True:
# #     for i in range(len(a)):
# #         sum+=int(a[i])**p
# #     test.append(sum)
# # print(test)




#테스트 케이스는 맞췄으나 runtime error(value error) 발생, 왜인지 모르겠음..?
#에러는 내가 a,p를 함께 받아주지 않아 생긴것이였다 -> 해결해줬으나 이제 오답임 
# def funct(a,p):
    
#     s=0
#     for i in list(str(a)):
#         s += int(i) ** p
#     return s
        

# a,p = map(int,input().split())

# number = [a]

# #반복되는 수가 100개 정도 안에서 나온다고 가정했을때(100개의 수열을 만들어냄) -> 이게 잘못인 것 같다함
# for i in range(100):
#     number.append(funct(number[i],p))

# for i in number:
#     cnt = number.count(i)
#     if cnt > 1:
#         idx = number.index(i)
#         length = len(number[:idx])
    
        

# print(length)



a,p = map(int, input().split())
number = [a]

while True:
    tmp = 0
    for i in str(number[-1]):
        tmp += int(i)**p
    if tmp in number:
        break
    number.append(tmp)

print(number.index(tmp))