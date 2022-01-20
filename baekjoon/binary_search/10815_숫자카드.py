#내가 구현하고자 한 것은 card에 있는 것들을 가지고 origin 이분탐색해서 있냐 없냐
#근데 실패
# N = 5
# origin = [6,3,2,10,-10]
# M = 8
# card = [10,9,-5,2,3,4,5,-10]

# origin.sort()

# correct = card[:]
# for i in card:
#     start = 0
#     end = len(origin)
#     while start <= end:
#         mid = (start+end)//2
#         if i == origin[mid]:
#             print(i)
#             break
#             # card[card.index(i)] = 0    
#         elif i < card[mid]:
#             end = mid-1
#         elif i > card[mid]:
#             start = mid+1
#         else:
#             card[card.index(i)] = 1 
            
    
# print(card)

#답지를 보았는데 매우 간단해서 슬프다
import sys
input = sys.stdin.readline
N = int(input())
origin = list(map(int, input().split()))
origin.sort()
M = int(input())
card = list(map(int, input().split()))


def binary_search(start, target, end):
    while start <= end:
        mid = (start+end)//2
        if target == origin[mid]:
            return 1
        elif target > origin[mid]:
            start = mid+1
        else:
            end = mid-1
    return 0 #if문에 해당하는게 없고 종료되면 0을 반환한다인가? 자리를 밖으로 나가니까 답이 나옴

for i in card:
    start = 0
    end = len(origin)-1 #start=0으로 해줬기때문에 -1해줘야함
    print(binary_search(start, i ,end),end=' ')










#다시 풀어봤는데 못풀었음
#로직 이해했다고 생각했는데 아니었음
#일단 반복문에 탈출하는 조건이 없었다
#start>end 이면 안도ㅑ
# import sys
# input = sys.stdin.readline
# M = int(input())
# card = list(map(int, input().split()))
# N = int(input())
# new = list(map(int, input().split()))
# card.sort()

# start = 0
# end = M-1
# def binary_code(start, end, target):
#     while start <= end:
#         mid = (start + end)//2
        
#         if target == card[mid]:
#             target = 1
#         elif target > card[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     target = 0    #왜 리턴이 아니라 타켓으로 주면 답이 달라질까?
#     print(target) 

# for i in new:
#     binary_code(start, end, i)

        
    