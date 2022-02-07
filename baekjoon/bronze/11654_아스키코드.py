#당연히 맞출거라 생각했는데 틀린 문제
#코테에서 값을 빠르게 받아주는 sys.stdin.readline 에는 개행문자가 받아지기 때문에 오른쪽에 개행문자를 삭제해야한다고 한다
import sys
input = sys.stdin.readline

print(ord(input().rstrip()))
