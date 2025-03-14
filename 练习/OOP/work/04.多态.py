#isinstance(object,classinfo ) 可以用来判断object对象是否属于classinfo类型  int float str class ————

class Employee:
    __name = None
    __mon_salary = None

    def __init__(self, __name, __mon_salary):
        self.__name = __name
        self.__mon_salary = __mon_salary

    def get_name(self):
        return self.__name

    def set_name(self, __name):
        self.__name = __name

    def get_mon_salary(self):
        return self.__mon_salary

    def set_mon_salary(self, __mon_salary):
        self.__mon_salary = __mon_salary
        
class Worker(Employee):
    def work(self):
        print("work")

    def get_annual(self):
        return self.get_mon_salary() * 12

class Manager(Employee):
    __bonus = None
    def __init__(self, __name, __mon_salary,__bonus):
        super().__init__(__name, __mon_salary)
        self.__bonus = __bonus

    def get_bonus(self):
        return self.__bonus

    def manage(self):
        print("manage")
    def get_annual(self):
        return super().get_mon_salary() * 12 + self.__bonus

def show_emp_annual(emp):
    annual = emp.get_annual()
    print("annual:", annual)

def Working(emp):
    if isinstance(emp, Worker):
        emp.work()
    else:
        emp.manage()

# 测试
worker = Worker("明", 8000)
manage =  Manager("红", 20000,100000)
show_emp_annual(worker)
show_emp_annual(manage)
Working(worker)
Working(manage)










