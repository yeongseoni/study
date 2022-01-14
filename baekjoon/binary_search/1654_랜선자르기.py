# #이코테의 코드와 완전 똑같음 ->응 틀렸어
# import sys
# input = sys.stdin.readline

# K,N = 4,11
# arr = [802, 743, 457, 539]
# # K,N = map(int,input().split())
# # arr = [int(input()) for i in range(K)]

# start = 0
# end = max(arr)

# result={}
# while (start <= end):
#     total = 0
#     mid = (start+end)//2 #다른 부분이라면 나눈걸로 해서 개수 구하는거
#     for i in arr:
#         total += i//mid
#     if total < N:
#         end = mid-1
#     else:
#         result = mid
#         start = mid+1
#     print(f'start:{start}, mid:{mid}, end:{end}')
# print(end)
# # print(max(result))
          
# #맞은 코드.. 왜 맞았니?
# #변경요소 : mid -> end, start=1
# import sys
# input = sys.stdin.readline

# # K,N = 4,11
# # arr = [802, 743, 457, 539]
# K,N = map(int,input().split())
# arr = [int(input()) for i in range(K)]

# start = 1
# end = max(arr)

# result=0
# while (start <= end):
#     total = 0
#     mid = (start+end)//2 #다른 부분이라면 나눈걸로 해서 개수 구하는거
#     for i in arr:
#         total += i//mid
#     if total < N:
#         end = mid-1
#     else:
#         result = mid
#         start = mid+1
# print(end)


#0어쩌구 에러남
#이해 못함. 왜 0을 1로 바꿔줘야 하는지와 왜 end값으로 해줘야 하는지??
import sys
input = sys.stdin.readline

K,N = 4,11
arr = [802, 743, 457, 539]
# K,N = map(int,input().split())
# arr = [int(input()) for i in range(K)]

start = 1
end = max(arr)

result=0
while (start <= end):
    total = 0
    mid = (start+end)//2 #다른 부분이라면 나눈걸로 해서 개수 구하는거
    for i in arr:
        total += i//mid
    if total < N:
        end = mid-1
    else:
        result = mid
        start = mid+1
    
print(result)

