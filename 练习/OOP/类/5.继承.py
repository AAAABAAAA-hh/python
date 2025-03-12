# 在子类的类名后加基类· 表示继承基类关系

class Student(object):
        def __init__(self, name,age,score,gender):
            self.name = name
            self.age = age
            self.score = score
            self.gender = gender

class Pupil(Student):
        def test_func(self):
                print("小学考试")
class Graduate(Student):
        def test_func(self):
                print("大学考试")

# python支持多重继承
class Teacher(Pupil, Graduate):
        pass















































































































