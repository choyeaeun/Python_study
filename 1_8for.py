
list = [1,2,3,4]

#for문 해당 리스트 돌면서 변수에 할당 반복
#순회할 리스트가 정해져 있을 때
for number in list:
    print(number)

#순회할 횟수가 정해져 있을 때
for num in range(5):
    print(num)

#len를 이용해 리스트의 길이를 불러오기
names = ['영희','철수', '예은','현지']
for i in range(len(names)):
    name = names[i]
    print('{}번째 학생 이름 : {}'.format(i+1, name))

#리스트가 있는 경우 순서와 값을 가져오는 enumerate
for i, name in enumerate(names):
    print('{}번째 학생 이름: {}'.format(i+1, name))