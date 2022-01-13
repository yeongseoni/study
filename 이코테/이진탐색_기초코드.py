#순차탐색:리스트 안에 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인
#이진탐색:**정렬되어 있는 리스트**에서 탐색 범위를 **절반씩** 좁혀가며 데이터를 탐색. 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정

#재귀 함수
import sys
input = sys.stdin.readline

def binary_fun(start, target, end, arr):
    print(end, start)
    if start>end:
        return None
    mid = (start + end)// 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_fun(start, target, mid-1, arr)
    else:
        return binary_fun(mid+1, target, end, arr)

    
n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = binary_fun(0, 7, n-1, arr)
print(result)

# def binary_fun2(start, target, end, arr):
#     while start <= end:
#         mid = (start + end) //2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             end = mid-1
#         else:
#             start = mid+1
#     return None