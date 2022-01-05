A = [1,5,2,1,4,3,5,2,1]
n = 10

dp = A[:]
for i in range(1,n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[j], dp[i]+A[j])
print(dp)