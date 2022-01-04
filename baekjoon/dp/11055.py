#내 풀이 -> 구현 못함
#n줄의 리스트를 작성해서 만약 다음값보다 크다면 다음 줄로 넘어가는 코드를 작성하고 싶었음
# n =10
# arr = [1,100,2,50,60,3,5,6,7,8]

#a1은 가장 작은 수라 가정
# s = [[0]*n for _ in range(n)]
# print(s)
# for i in range(n):
#     s[i][0] = arr[0]

# for i in range(n):
#     for j in range(1,n):
#         if arr[j] > arr[j-1]:  
#             s[i][j] = s[i][j-1] + arr[j]
#         else:
#             s[i+1][j+1] = s[i+1][j-1] + arr[j+1]


#답지 아이디어 구현 - > 못함 ㅎㅎ
n = 10
arr = [1,100,2,50,60,3,5,6,7,8]
dp = arr[:]

for i in range(1,10):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[i]+arr[j])

print(dp)