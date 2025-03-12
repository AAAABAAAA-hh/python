class A:
    n1 = 200

class B(A):
    #重写父类的属性n1
    n1 = 300

class Person:
    name = None
    age = None
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print(f'{self.name} says {self.age} years old')

class Student(Person):
    id = None
    score = None
    def __init__(self, name, age,  id , score):
        super().__init__(name, age)
        self.id = id
        self.score = score
    def say(self):
        print(f'{self.name} says {self.age} years old', self.score, self.id)




















