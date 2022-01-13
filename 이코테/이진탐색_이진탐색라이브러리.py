#bisect_left(a,x):정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
#bisect_right(a,x):정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

from bisect import bisect_left, bisect_right
a = [1,2,3,4,4,6,7]

print(bisect_left(a,4))
print(bisect_right(a,4))

#값이 특정 범위에 속하는 데이터 개수 구하기
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    print(f'right:{right_index}, left:{left_index}')
    return right_index-left_index

a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))

#파라메트릭 서치:최적화 문제를 결정 문제(예 혹은 아니오)로 바꾸어 해결하는 기법
#ex:특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
#일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결