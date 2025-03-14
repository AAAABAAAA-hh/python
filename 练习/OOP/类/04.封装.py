# 以公司职员信息为例子

class Clerk(object):
    # 公共属性
    name = None
    # 私有属性
    __job = None
    __salary = None
    def __init__(self, name, job, salary):
        self.name = name
        self.__job = job
        self.__salary = salary
    #提供公共的方法来对私有属性进行访问
    def set_job(self, job):
        self.__job = job
    def get_job(self):
        return self.__job
    #私有方法
    def __hi(self):
        print("hi")
    #公有方法来调用私有方法
    def f1(self):
        self.__hi()

clerk = Clerk("tiger","Python工程师",20000)
# 公共属性在外部可以直接访问
print(clerk.name)
# 私有属性 不可直接访问
# print(clerk.__job)
print(clerk.get_job())




















































































































