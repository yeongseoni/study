#첫번째 풀이
# t = int(input())
# for i in range(t):
#     h,w,n = map(int, input().split())

#     if (n%h) == 0:
#         floor = (n // h) * 100
#     else:
#         floor = (n % h) * 100

#     count = (n // h) + 1

#     answer = floor + count

#     print(answer)

#두번째, 리스트 이용할거
t = int(input())

for i in range(t):
    h,w,n = map(int, input().split())
    
    hotel_list = []
    for count in range(1,w+1):
        for floor in range(1,h+1):
            what = (floor * 100) + count
            hotel_list.append(what)
    print(hotel_list[n-1])

