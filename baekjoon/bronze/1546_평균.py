N = int(input())
score = list(map(int, input().split()))
max_num = max(score)

for i in range(len(score)):
    score[i] = score[i]/max_num*100
print(sum(score)/N)