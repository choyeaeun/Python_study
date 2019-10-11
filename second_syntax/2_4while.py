
#  while문 
selected = None
#while selected not in ['가위', '바위', '보']:
 #   selected = input('가위, 바위, 보 중에 선택하세요>')
print(selected)

# break
list = [1, 2, 3, 4, 5, 7, 2, 5, 237, 55]
for i in list:
    if i % 3 == 0:
        print(i)
        break
    
# try except
try:
    import my_module
except ImportError:
    print('모듈이 없습니다.')
# except Exception as ex: 로 하면 ex에 어떤 에러인지 담아서 출력 가능

# raise문으로 에러 발생시키기
school = {'1반': [198, 128, 174, 187], '2반': [188, 190, 187, 167]}
try: 
    for class_num, students in school.items():
        for student in students:
            if student >= 190:
                print(class_num, '에 190이상이 있습니다.')
                # break # 한번만 실행시키고 싶지만 반복문이 두 개 이므로 모두 빠져 나가기 힘듦
                raise StopIteration
except StopIteration:
    print('정상종료')
