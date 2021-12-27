# #내가 푼거 근데 안돼
# def func(arr):
#   x,y = 0,0
#   sum_list = []

#   nx,ny=0,0
  
#   for i in range(n):
#     sum=0
#     for j in range(n):
#       if nx>n or ny>n:
#         continue
#       sum += arr[y][x]
      
#       nx = x+dx[j]
#       ny = y+dy[j]

#       sum += arr[ny][nx]
      
#     sum_list.append(sum)
#   print(sum_list) 
  


# arr = [[1, 1, 1, 0, 0, 0],
#       [0, 1, 0, 0, 0, 0], 
#       [1, 1, 1, 0, 0, 0],
#       [0, 0, 2, 4, 4, 0],
#       [0, 0, 0, 2, 0, 0],
#       [0, 0, 1, 2, 4, 0]]
# n = len(arr)

# dx = [1,2,1,0,1,2]
# dy = [0,0,1,2,2,2]

# func(arr)


#남의 답

def hourglasses(arr, i ,j):
    return sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+2])


arr = [[1, 1, 1, 0, 0, 0],
      [0, 1, 0, 0, 0, 0], 
      [1, 1, 1, 0, 0, 0],
      [0, 0, 2, 4, 4, 0],
      [0, 0, 0, 2, 0, 0],
      [0, 0, 1, 2, 4, 0]]


ans = hourglasses(arr, 0,0)
for i in range(4):
    for j in range(4):
        ans = max(ans, hourglasses(arr, i, j))

print(ans)
