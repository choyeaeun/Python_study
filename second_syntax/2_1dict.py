#list와 비슷한 dictionary 활용법

#dict선언 : 중괄호
dict = { 'one' : 1, 'two' : 2, 'three' : 3}
print(dict)

#추가 / list에서는 이렇게 추가 불가능(append로만)
dict['four'] = 4
print(dict)

#수정 
dict['three'] = 33
print(dict)

#삭제
del dict['one']
print(dict)
#pop은 pop하는 수를 찍어줌
print(dict.pop('three'))


#for문
#키값 가져오기
for key in dict.keys():
    print(key)
#벨류값 가져오기
for value in dict.values():
    print(value)
#키와 벨류 값 모두 가져오기
for key, value in dict.items():
    print(key, value)


#딕셔너리 합치기 -> 덮어쓰기 때문에 순서가 매우 중요
#1
dict1 = {1:100, 2:200}
dict2 = {1:1000, 3:300}

dict1.update(dict2)
print(dict1)
#2
dict1 = {1:100, 2:200}
dict2 = {1:1000, 3:300}

dict2.update(dict1)
print(dict2)