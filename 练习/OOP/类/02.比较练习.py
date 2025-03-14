# 比较 人之间是否相等

class Person:
    age = None
    name = None
    def compare1(self, p):
        flag = False
        if self.age == p.age:
            flag = True
        else:
            return False
        if flag:
            if self.name == p.name:
                return True
            else:
                return False
    def compare2(self, p):
        if self.age == p.age and self.name == p.name:
            return True
        else:
            return False
p1 = Person()
p2 = Person()
p1.age = input("输入第一个人的年龄")
p2.age = input("输入第二个人的年龄")
p1.name = input("输入第一个人的名字")
p2.name = input("输入第二个人的名字")

print(f"比较的结果为：{p1.compare1(p2)}")
print(f"比较的结果为：{p1.compare2(p2)}")



















