import sys
input = sys.stdin.readline
word = list(input().rstrip())
alphabet = [chr(i) for i in range(97, 123)]

for i in alphabet:
    if i in word:
        print(word.index(i),end=' ')
    else:
        print(-1,end=' ')

#다른사람의 풀이가 더 좋은듯
#find함수는 어떤 찾는 문자가 문자열 안에서 첫번째에 위치한 순서를 숫자로 출력한다

word = input().rstrip()
alpahbet = list(range(97,123)) #range만 해줘도 리스트에 들어가는구나

for i in alpahbet:
    print(word.find(chr(i)), end=' ')
