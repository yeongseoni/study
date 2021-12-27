#10951
while 1:
  try:
    a,b = map(int, input().split())
    print(a+b)
  except:
    break

#try문:잠재적인 예외 처리하기
#except문:예외 발생시 실행할 코드
#10952
while 1:
  a,b = map(int, input().split())
  if a+b == 0:
    break
  if a == False or b==False:
    break
  print(a+b)

#11021
n = int(input())

for i in range(1,n+1):
    a,b = map(int, input().split())
    print(f'Case #{i}: {a+b}')

#11022
n = int(input())

for i in range(1,n+1):
    a,b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')

#1924

#8393
n = int(input())
lists = [ i for i in range(1,n+1)]
print(sum(lists))

#2446
#내가 한거
n = int(input())

for i in range(n):
    print(' '*i + '*'*(9-(2*i)) + ' '*i)
for i in range(n-2,-1,-1):
    print(' '*i + '*'*(9-(2*i)) + ' '*i)

#일반화
n = int(input())

for i in range(n):
    print(' '*i + '*'*((n-i)*2-1))
for i in range(n-2,-1,-1):
    print(' '*i + '*'*((n-i)*2-1))


