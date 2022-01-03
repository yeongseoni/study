#1463
# n = int(input())
# cnt = 0

# while n > 1:
#   if n % 3 == 0:
#     n = n//3
#     cnt += 1
#   elif n % 2 == 0:
#     n = n//2
#     cnt += 1 
#   else:
#     n -= 1
#     cnt += 1
# print(cnt)

#11726
# n=3
# test = [[0]*n for i in range(2)]
# print(test)

# for i in range(2):
#   for j in range(0, 3, 2):
#     print(i,j)
#     test[i][j] +=1
# print(test)
    

#11727
#내 풀이 -> 틀림
# n = int(input())

# arr=[10001]*(n+1)
# arr[1] = 1
# arr[2] = 3
# for i in range(2,n+1):
#     if arr[i] == 10001:
#         arr[i] = arr[i-1] + arr[i-2]*2
# print(arr[n] % 10007)

#답지
# n=int(input())

# arr = [0,1,3] + [0] *(n-2)


# for i in range(3, n+1):
#     arr[i] = arr[i-1] + arr[i-2]*2

# print(arr[n]%10007)

#9095
#규칙을 못찾았음.. 수학을 못하는게 아닐까?
t = int(input())

for i in range(t):
  
  n = int(input())
  arr = [0,1,2,4] + [0] * (n-2)
  
  for i in range(4,n+1):
    arr[i] = arr[i-3] + arr[i-2] + arr[i-1]
  print(arr[n])

