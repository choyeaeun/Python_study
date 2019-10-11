
# 클래스
class Human():
    
    # 초기화 함수
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    # 클래스 호출하면 실행되는 문자열 함수
    def __str__(self):
        return '{} (몸무게 {}kg)'.format(self.name, self.weight)

    def eat(self):
        self.weight += 0.1
        print('{}가 많이 먹어서 {}kg이 되었습니다.'.format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print('{}가 많이 걸어서 {}kg이 되었습니다.'.format(self.name, self.weight))

person = Human('예은', 70.0)
print(person)
person.eat()
print(person)