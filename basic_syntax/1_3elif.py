rock = '바위'
scissors = '가위'
paper = '보'

mine = rock
yours = paper

win = '이김'
draw = '비김'
lose = '짐'

if mine == yours:
    #result 선언 안하고 바로 써버리기
    result = draw
else:
    if mine == scissors:
        if yours == rock:
            result = lose
        else:
            result = win
    elif mine == rock:
        if yours == paper:
            result = lose
        else:
            result = win
    elif mine == paper:
        if yours == scissors:
            result = lose
        else:
            result = win

print(result)
