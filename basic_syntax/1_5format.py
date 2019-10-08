
name = '조예은'
age = 24

sentence = '내 이름은 {} 입니다. 내 나이는  {} 살 입니다.'
#format은 문자열에 대한 여러 기능이 담긴 함수 
#문자열에 포함된 중괄호를 format 뒤에 있는 소괄호 변수로 치환
perfect = sentence.format(name, age)
print(perfect)

place = 'starbucks'
goto = 'toilet'
print('이 장소는 {}입니다. 지금은 {}에 가고 싶습니다.'.format(place, goto))