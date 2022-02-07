a,b = input().split()
a = a[::-1] #역순으로 정렬
b = b[::-1]
if int(a)>int(b):
  print(a)
else:
  print(b)