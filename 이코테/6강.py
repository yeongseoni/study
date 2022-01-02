#개미전사
#내가 구현
# n = int(input())
# block = list(map(int, input().split()))

# s = [0 for i in range(n-2)]
# for i in range(n):
#   for j in range(i+2, n):
#     if s[i] != 0:
#       s[i] = max(s[i], block[i]+block[j])
#     s[i] = block[i]+block[j]
# print(max(s))

#정답
# n = int(input())

# arr = list(map(int, input().split()))

# d = [0] * 100

# d[0] = arr[0]
# d[1] = max(arr[0], arr[1])
# for i in range(2, n):
#   d[i] = max(d[i-1], d[i-2]+arr[i])

# print(d[n-1])

#1로 만들기
# n = int(input())

# arr = [0] * (n+1)
# for i in range(2,n+1):
#   arr[i] = arr[i-1] + 1
#   if i%5 == 0:
#     arr[i] = min(arr[i], arr[i//5]+1)
#   if i%3 == 0:
#     arr[i] = min(arr[i], (arr[i//3]+1))
#   if i%2 == 0:
#     arr[i] = min(arr[i], arr[i//2]+1)
# print(arr[n])

#효율적인 화폐구성
#내가 한거 틀림
# n,m = 2,7

# num=[]
# for i in range(n):
#   num.append(int(input()))
# num.sort(reverse=True)

# cnt=0
# while m>1:
#   for i in num:
#     m -= i
#     cnt+=1
#     if m % i == 0:
#       m = m//i
#       cnt+=1
#     else:
#       cnt = -1
#   print(cnt)
    
#답지
n,m = map(int, input().split())
print(n)
a,b = int(input.split())
print(a)