T = int(input())

for i in range(T):
    s = list(input().split())
    R = s.pop(0)
    
    for i in s:
        for j in i:
            print(j*int(R), end='')
        print() #이거때문에 틀렸다 ..
        
        
#다른사람 코드
#리스트를 만들어줄 필요가 없었다
for i in range(T):
    n,s = input().split()
    test= ""
    for i in s:
        test += int(n)*i
    print(test)



