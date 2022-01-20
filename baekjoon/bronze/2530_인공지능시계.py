
#틀린 이유 = 초의 범위가 크기 때문에 단순히 h-24로 해주면 60시간이 넘어가는 경우 해결 못함
#%를 사용해서 해결, 나는 %가 아직도 헷갈리나봐... 나머지다
import sys
input=sys.stdin.readline

A,B,C=map(int, input().split())
D =int(input())

C += D
if C >= 60:
    B += (C//60)
    C = (C%60)
if B >= 60:
    A += (B//60)
    B = (B%60)
if A >= 24:
    A = (A%24)
print(A, B, C)

