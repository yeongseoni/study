#처음에는 단순히 주어진 배열에서 내림차순해서 세트로 변환하고 길이만 반환하면 된다 생각
#왜 그랬지? 줄어드는 수에 집중했어야함
# n = int(input())
# A = [10,30,10,20,20,10]

# s = set(sorted(A, reverse=True))
# print(len(s))



n = int(input())
A = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))