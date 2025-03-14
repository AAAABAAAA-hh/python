class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Food:
    def __init__(self, name):
        self.name = name

class Fish(Food):
    pass

class Bone(Food):
    pass

def feed(animal: Animal, food: Food):
    print(f"动物 {animal.name} 要喂食的食物是 {food.name}")

#测试
dog_1 = Dog("大黄狗")
cat_1 = Cat("白猫")
fish_1 = Fish("草鱼")
bone_1 = Bone("棒骨")
feed(dog_1, bone_1)
feed(cat_1, fish_1)











