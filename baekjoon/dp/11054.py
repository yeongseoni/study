#아이디어를 봐도 구현을 못한다
arr = [1,5,2,1,4,3,4,5,2,1]
n = 10

#나는 최대값이 되도록 하는 원소들을 따로 리스트에 넣는 방식을 하려했는데 안됐음
#해설에서는 더한 개수로 풀었다
increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j]+1)
#구하는 기준이 오른쪽이다
#오른쪽에서부터 비교를 해야하기 때문에 reverse를 해주는 듯
for i in range(n-1, -1, -1):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [i+j-1 for i,j in zip(increase, decrease)]
print(max(result))


