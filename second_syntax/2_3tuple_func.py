
# 튜플을 이용하여 함수의 리턴

# 리스트
list = [1, 2, 3, 4, 5]
for i, v in enumerate(list):
    print('{}번째 값 : {}'.format(i, v))
for a in enumerate(list):
    #print('{}번째 값 : {}'.format(a[0], a[1]))
    print('{}번째 값 : {}'.format(*a))

# 딕셔너리
dict = {'one' : 1, 'two' : 2, 'three' : 3}
for key, value in dict.items():
    print('{}는 {}'.format(key, value))

for a in dict.items():
    #print('{}는 {}'.format(a[0], a[1]))
    print('{}는 {}'.format(*a))