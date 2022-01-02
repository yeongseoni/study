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
n = int(input())

arr = list(map(int, input().split()))

d = [0] * 100

d[0] = arr[0]
d[1] = arr[1]
for i in range(2, n):
  d[i] = max(d[i-1], d[i-2]+arr[i])

print(d[n-1])