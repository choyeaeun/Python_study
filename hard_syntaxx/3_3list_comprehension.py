
# 원래 사용하는 코드 
area1 = []
for i in range(1, 15):
    if i % 2 == 0:
        area1 = area1 + [i * i]
print(area1)

# comprehension 코드 
area2 = [i * i for i in range(1, 15) if i % 2 == 0]
print(area2)

list1 = [(x, y) for x in range(15) for y in range(15)]
#print(list1)

# dictionary
student = ['a', 'b', 'c', 'd']
for num, name in enumerate(student):
    print('{}번의 이름은 {}'.format(num + 1, name))

# dictionary comprehension
student_dict = { '{}번'.format(num+1) : name for num, name in enumerate(student)}
print(student_dict)

# 두 개의 리스트 합쳐서 출력
scores = [100, 39, 69, 80]
for name, score in zip(student, scores):
    print(name, score)

# 두 개의 리스트 하나의 딕셔너리에 합치기
score = { name : score for name, score in zip(student, scores)}
print(score)