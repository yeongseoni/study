

# N=10
# card = [6,3,2,10,10,10,-10,-10,7,3]
# M=8
# prob = [10,9,-5,2,3,4,5,-10]
# prob.sort()

# cnt = [0 for _ in range(8)]
# def binary_search(start, target, end):
#     print(mid)
#     mid = (start+end)//2
#     print(mid)
#     while start <= end:
#         if target == prob[mid]:
#             cnt[mid]+=1
#         elif target > prob[mid]:
#             start = mid+1 
#         else:
#             end = mid-1
#     cnt[mid] = 0
            
        
        
# start = 0
# end = M-1
# for i in card:
#     print(i)
#     binary_search(start, i, end)
# print(cnt)
        
#내가 구현하고 싶은거
#가지고 있는 카드 원소들을 하나씩 돌려서 있는지 확인하는거


# def binary_search(start, target, end, prob):
#     mid = (start+end)//2
#     while start <= end:
#         if target == prob[mid]:
#             return 1
#         elif target > prob[mid]:
#             start = mid+1 
#         else:
#             end = mid-1
#     return 0
    
# N=10
# card = [6,3,2,10,10,10,-10,-10,7,3]
# M=8
# prob = [10,9,-5,2,3,4,5,-10]
# prob.sort()



# for i in card:
#     start = 0
#     end = M-1
#     print(binary_search(start, i, end, prob), end=' ')
    
#결국 답을 보는데 다들 왜이렇게 어렵게 짜죠..?
#그나마 이코테에서 배운 라이브러리 아이디어를 가져와서 해보겠다
# from bisect import bisect_left, bisect_right

# N=10
# card = [6,3,2,10,10,10,-10,-10,7,3]
# M=8
# prob = [10,9,-5,2,3,4,5,-10]
# card.sort()
# print(card)

# def find_count(target):
#     left_idx = bisect_left(card, target)
#     right_idx = bisect_right(card, target)
#     # if left_idx - right_idx == 0:
#     #     return 0   #응 괜히 줬어~ 왜 줌? 
#     return right_idx - left_idx

# for i in prob:
#     print(find_count(i), end=' ')
    
    
# #중복요소를 카운팅하는 법에는 여러가지가 있다
# #딕셔너리를 사용하기도 하는데, 내가 몰랐던 방법이기에 써본다
# #try _ except문을 사용했고, 나는 아직 여기를 잘 모른다

# count = {}
# lists = [6,3,2,10,10,10,-10,-10,7,3]
# for i in lists:
#     try: count[i] += 1
#     except: count[i] = 1
# print(count)





from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
# card = [6,3,2,10,10,10,-10,-10,7,3]
# new = [10,9,-5,2,3,4,5,-10]
M=int(input())
card = list(map(int, input().split()))
N=int(input())
new = list(map(int, input().split()))

card.sort()

def binary_code(start, end, target):
    while start <= end:
        mid = (start+end)//2
        
        if target == card[mid]:
            left = bisect_left(card, target)
            right = bisect_right(card, target)
            return right - left
        elif target > card[mid]:
            start = mid+1
        else:
            end = mid -1
    return 0

start=0
end = M-1
for i in new:
    print(binary_code(start, end, i), end= ' ')
            



#count 사용했는데 시간초과! 
# M = int(input())
# card = [map(int, input().split())]
# N = int(input())
# new = [map(int, input().split())]
# # card = [6,3,2,10,10,10,-10,-10,7,3]
# # new = [10,9,-5,2,3,4,5,-10]

# card.sort()

# for i in new:
#     print(i)
#     print(card.count(i), end= ' ')

#counter 쓰는거 편한듯?
# 3
# from collections import Counter
# import sys
# input = sys.stdin.readline
# n = int(input())
# n_num = list(map(int, input().split()))
# m = int(input())
# m_num = list(map(int, input().split()))
# n_num = Counter(n_num)
# for i in m_num:
#      print(n_num[i], end=" ")

