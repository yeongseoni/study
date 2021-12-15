#단순하게 가장 먼저 나오는 수의 범위를 리스트로 구현해서 다음 나오는 쌍이 그 안에 들어가나?
#안들어간다면 새로 만들고 해당 수의 범위를 붙여주는건데 10점 나옴
def solution(routes):
    a = [i for i in range(routes[0][0],routes[0][1]+1)]
    
    cnt=1
    for i in range(1,len(routes)):
        if routes[i][0] not in a and routes[i][1] not in a:
            cnt+=1
            a.extend([i for i in range(routes[i][0],routes[i][1]+1)])
            
    return cnt

#남의 풀이
def solution2(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    camera=-30001

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer

