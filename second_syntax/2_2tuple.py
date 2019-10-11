
# 튜플은 소괄호로 선언하며, 값의 변경과 삭제가 불가능

# 튜플 선언
tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3, 4
print(tuple1)
print(tuple2)

# 리스트를 튜플에 넣을 수도 있음
list1 = [4, 5, 6, 7]
tuple3 = tuple(list1)
print(tuple3)

# packing, unpacking : 여러 개의 값을 한 번에 변수에 넣을 수 있다
c = (3, 4)
a, b = c
print(a) # 3
print(b) # 4

# temp없이 바로 두 개의 값 바꾸기 가능
amy = 10
bella = 13
amy, bella = bella, amy
print(amy) # 13
print(bella) # 10
