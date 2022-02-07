import sys 
input=sys.stdin.readline
n = int(input())

for i in range(n):
    score = list(map(int, input().split()))
    N = score.pop(0)
    score2 = [1 for i in score if i>sum(score)/N]
    print(f'{(sum(score2)/N)*100:.3f}%')   #소숫점 자릿수 지정해주는거 :쓰고 자릿수 지정
