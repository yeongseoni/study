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

import sys
input = sys.stdin.readline
N,M = map(int, input().split())
a = list(map(int, input().split()))
        
