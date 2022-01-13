#대충 코드, 동작은 하네요...
# N,M=4,6
# a = [19,15,10,17]
# a.sort() #정리된 배열로 변경

# result = {}
# for i in range(a[0], a[-1]+1):
#     cnt = a[:]
#     for j in range(4):
#         cnt[j] -= i
#         if cnt[j] <0 :
#             cnt[j] = 0
#     if sum(cnt) >= M:
#         result[i] = cnt
# print(max(result))

#나의 코드는 이진 탐색을 전혀 사용하지 않았다
#그냥 최소값 중에 걸리지 않을까라는 생각이었음
import sys
input = sys.stdin.readline #이것을 암기해 놓자...
# N,M = map(int, input().split())
# a = list(map(int, input().split())) #배열받기
# a.sort()

# result = {} #라이브러리를 사용해줌
# for i in range(a[0], a[-1]+1):
#     cnt = a[:]
#     for j in range(N):
#         cnt[j] -= i
#         if cnt[j] <0 :
#             cnt[j] = 0
#     if sum(cnt) >= M:
#         result[i] = cnt
# print(max(result))

#<<<<해설>>>>
#절단기의 높이는 0부터 10억까지의 정수 중 하나이다 -> 이렇게 큰 탐색 범위를 보면 가장 먼저 **이진탐색**을 떠올릴 것
#시작점:0 끝점:19 중간점:9
#중간점의 값은 시간이 지날수록 '최적화된 값'이 된다

N,M=4,6
arr = [19,15,10,17]
start = 0
end = max(arr)

result = 0
while (start <= end):
    total = 0
    mid = (start + end)//2
    for i in arr:
        if i > mid:
            total += i-mid
    if total < M:
        end = mid-1
    else:
        result = mid
        start = mid+1
    print(f'start:{start}, mid:{mid}, end:{end}')
print(result)
        
    



#구현해보려고 했으나 실패.. 왜일까?
# def binary_code(start, end, arr):
#     if start > end:
#         return False
#     mid = (start + end)//2
#     for i in range(N):
#         arr[i] -= mid
#         if sum(arr)  == M:
#             return mid
#         elif sum(arr) > M:
#             return binary_code(mid+1, end, arr)
#         else:
#             return binary_code(start, mid-1, arr)
       
    



# N,M=4,6
# arr = [19,15,10,17]
# arr.sort()

# print(binary_code(0, arr[-1], arr))

