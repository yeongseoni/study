#뭐가 틀렸는지 모르겠음 ->알아냄

import sys
input = sys.stdin.readline

A,B = map(int, input().split())
C = int(input())

def clock(hour, minute, cook):
    minute += cook
    if minute >= 60:
        hour += (minute//60)
        minute = (minute%60)
        
    if hour >= 24: #h >= 24 일때로 조건을 줬어야했는데 23으로 주니 당연히 틀림
        hour = hour -24
    print(hour, minute)

clock(A,B,C)

            