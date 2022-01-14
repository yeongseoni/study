

N=10
card = [6,3,2,10,10,10,-10,-10,7,3]
M=8
prob = [10,9,-5,2,3,4,5,-10]

prob.sort()
print(M)
cnt = [0 for _ in range(M)]
def binary_search(start, target, end):
    mid = (start+end)//2
    print(mid)
    while start <= end:
        if target == prob[mid]:
            cnt[mid]+=1
        elif target > prob[mid]:
            start = mid+1 
        else:
            end = mid-1
    cnt[mid] = 0
            
        
        
start = 0
end = M-1
for i in card:
    binary_search(start, i, end)
    print(cnt)
        
print('hello')