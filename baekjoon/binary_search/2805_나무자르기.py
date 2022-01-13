#랜선 자르기랑 똑같지 않나..?
#직접 손으로 풀어보니까 마지막에 끝날때 end값이 15가 되고 끝남
#근데 이걸 설명은 못하겠다..?
#출발을 1로 놓는 것은 아무래도 나무의 높이가 0일 수는 없으니까? 맞나?

# N,M =4,7
# arr = [20, 15, 10, 17]
import sys
input = sys.stdin.readline
N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort() #시간초과가 나서 설마 정렬을 해달라는거..?하면서 했는데 통과.. 근데 이제 pypy로 하면 된다네..? 굳이 할 필요는 없을듯하다

start = 1
end = max(arr)
while start <= end:
    mid = (start+end)//2
    total = 0
    for i in arr:
        if i > mid:
            total += i-mid
    if total >= M:
        start = mid+1
    else:
        end = mid-1
print(end)
    
