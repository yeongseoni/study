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
n=3
test = [[0]*n for i in range(2)]
print(test)

for i in range(2):
  for j in range(0, 3, 2):
    print(i,j)
    test[i][j] +=1
print(test)
    

