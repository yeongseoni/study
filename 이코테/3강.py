#재귀함수:자기 자신을 다시 호출하는 함수
#스택을 사용해야 할 때 스택 라이브러리 대신에 재귀함수를 이용하는 경우가 많다

def recursive_function():
    print("재귀함수를 호출합니다")
    recursive_function()

    
recursive_function()


#종료조건이 있는 재귀함수
#(1번째(2번째(3번쨰...(99번째(100번째))))) 이런식으로 호출되기 때문에 99번째 종료 - 98번째 종료 이렇게 나옴
def recursive_function(i):
    
    if i==100:
        return
    print(i,'번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료합니다.')

recursive_function(1)

#반복문 이용한 팩토리얼 구현
def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

#재귀적으로 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    
    return n * factorial_recursive(n-1)

print("반복으로 구현:",factorial_iterative(6))
print("재귀로 구현:", factorial_recursive(6))

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        print(a,b)
        return gcd(b, a%b)
print(gcd(162, 192))


#dfs : 깊이 우선 탐색, 깊은 부분을 우선적으로 탐색하는 알고리즘
#스택 자료구조(혹은 재귀함수)를 이용
#1.탐색 시작 노드 스택에 삽입하고 방문처리
#2.스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드 스택에 넣고 방문처리, 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
#3.더이상 2번의 과정을 수행할 수 없을때까지 반복


