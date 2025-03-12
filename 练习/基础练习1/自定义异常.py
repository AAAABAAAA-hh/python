class AgeError(Exception):
    pass


class Person:
    def __init__(self, name, age):
        if not  18<=age<=65:
            raise AgeError("年龄需要在 18 - 65 之间")
            print()
        else:
            self.name = name
        self.age = age

person_1 =  Person("mign",11)
person_2 = Person("mgn",30)




















