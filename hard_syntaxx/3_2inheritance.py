
class Animal():
    
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('먹는다')

    def walk(self):
        print('걷는다')

    def greet(self):
        print('인사한다')

class Human(Animal):
    
    def __init__(self, name, hand):
        super().__init__(name)
        self.hand = hand

    def wave(self):
        print('손을 흔든다')

    # overiding
    def greet(self):
        self.wave
        # 부모의 값 가져오기
        super().greet()

class Dog(Animal):
    def wag(self):
        print('꼬리를 흔든다')

    # overiding
    def greet(self):
        self.wag

person = Human('예은이가','오른')
person.eat()
person.walk()
person.wave()

malon = Dog('malon')
malon.eat()
malon.walk()
malon.wag()