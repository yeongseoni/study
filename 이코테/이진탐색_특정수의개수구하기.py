from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

#내가 구현한거
N,x = map(int, input().split())
arr = list(map(int, input().split()))

if (bisect_right(arr,x) - bisect_left(arr,x)) == 0:
    print(-1)
else:
    print(bisect_right(arr,x) - bisect_left(arr,x))

#동빈나의 구현
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

count = count_by_range(array, x,x) #x가 두번 들어간다는 생각을 못했음 

if count == 0:
    print(-1)
else:
    print(count)