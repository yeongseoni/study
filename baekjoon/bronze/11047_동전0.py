import sys
input = sys.stdin.readline
K, W = list(map(int, input().split()))

money = list(int(input()) for _ in range(K))
money.sort(reverse=True)

for i in range(K):
    if money[i] > W:
        pass
    elif money[i] <= W:
        W//money[i]
        
        
        
        
        
        
        
        
        
        
# n = 1260
# count = 0

# type = [500, 100, 50, 10]

# for coin in type:
#     count += n // coin
#     n %= coin

# print(count)