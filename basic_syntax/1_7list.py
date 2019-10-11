
#헐 리스트에 마지막에서 몇번째를 찾을 때는 list[-n]으로 찾기
rainbow = ['빨','주','노','초','파','남','보']
my_favorite = rainbow[-1]
print('내가 가장 좋아하는 색은 {}입니다.'.format(my_favorite))

#append를 이용해서 값 추가하기
rainbow.append('형광')
print(rainbow)

#list끼리 연결하기
list2 = rainbow + rainbow
list2.extend(rainbow)
print(list2)

#list안에 특정 값 있는지 검색
n = '흰'
whatIs = n in list2
print(whatIs)

old = '보'
if old in rainbow:
    print('내 안에 {}있다.'.format(old))

#순서로 지우기
del rainbow[1]
print(rainbow)

#특정값 지우기
rainbow.remove('남')
print(rainbow)