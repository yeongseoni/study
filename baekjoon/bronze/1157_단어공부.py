#보자마자 생각난 건 소문자로 다 바꿔버리고 카운트해서 출력
# word = ['Mississipi']
# word = [input().lower()]
# word = 'Mississipi'.lower()

# cnt = dict()
# for i in word:
#     cnt[i] = word.count(i)


# cnt2 = {1 if cnt[i]>=max(cnt.values()) else 0 for i in cnt}
# print(cnt2)
# res=[1 if cnt[i]>=max(cnt.values()) else 0 for i in cnt]
# print(res)



# test = set(word)
# print(test)
# cnt=[0 for i in word]

# for i in word:
#     cnt.append(word.count(i))
# res=[1 if i>= max(cnt) else 0 for i in cnt]
# print(res)

# if sum(res)>1:
#     print('?')
# else:
#     print()


#30분동안 구현 못해서 다른 사람 코드를 보기로 함
word = input().upper()
unique = list(set(word))  #세트 해주고 리스트로 해주면 인덱스 사용 가능하다
cnt = []
for i in unique:
    cnt.append(word.count(i))
print(cnt)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(unique[cnt.index(max(cnt))])


