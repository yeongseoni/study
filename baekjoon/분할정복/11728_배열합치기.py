#맞기는 했는데 살짝 old한 생각이라고 생각한...
import sys
input=sys.stdin.readline
N,M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A+B
C.sort()
for i in C:
    print(i, end= ' ')
    
#' '.join 이용해서 1 2 3 이런식으로 출력이 가능하구나..
print(' '.join(map(str, new)))