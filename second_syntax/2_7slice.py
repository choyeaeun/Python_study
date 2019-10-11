
# 리스트의 구간을 가져오기
# slice는 구간을 가져오면서 복사하는 것.(새로 생성)
list1 = [1, 45, 765, 34, 9, 234]
# list1의 1번째부터 3번째 전까지의 값을 들고옴
list2 = list1[1 : 3]
print(list2) # [45, 765]

# 처음부터 4번째 전까지의 값
list3 = list1[ : 4]
print(list3) # [1, 45, 765, 34]

# 2씩 띄어서 가져오기
list4 = list1[ : :2]
print(list4)
# 역행으로 가져오고 싶을 때는
list5 = list1[ : : -1]
print(list5)

# 지우기 가능
del list5[2:4]
print(list5)

# 수정도 가능
list2[1:3] = [22, 33, 44]
list3[ :4] = [11, 22, 77]
print(list2,list3)
