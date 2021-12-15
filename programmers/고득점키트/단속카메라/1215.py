def solution(routes):
    a = [i for i in range(routes[0][0],routes[0][1]+1)]
    
    cnt=1
    for i in range(1,len(routes)):
        if routes[i][0] not in a and routes[i][1] not in a:
            cnt+=1
            a.extend([i for i in range(routes[i][0],routes[i][1]+1)])
            
    return cnt
