class Monster:
    name = 'Mon'
    age = 200

    def func(self):
        print(self.name, self.age)

print(Monster)
print(Monster.name,Monster.age)


#抽象类
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #eat 就是抽象方法
    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):
    def eat(self):
        print("吃屎")

dog = Dog("huang",20)
dog.eat()






















