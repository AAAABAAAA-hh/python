#    电脑属性
class Computer:
    cpu = None
    mem = None
    disk = None
    def __init__(self, cpu, mem, disk):
        self.cpu = cpu
        self.mem = mem
        self.disk = disk
    def get_details(self):
        print("cpu:", self.cpu, "mem:", self.mem, "disk:", self.disk)

class PC(Computer):
        brand = None
        def __init__(self, cpu, mem, disk,brand):
            super().__init__(cpu,mem,disk)
            #self.brand 属于子类本身特殊属性初始化
            self.brand = brand


class NotePad(Computer):
        color = None

com_1 = PC(1,1,1,1)
print(com_1.cpu, com_1.mem, com_1.disk, com_1.brand)
com_2 = NotePad(2,2,2)
com_2.color = "red"
com_1.get_details()
com_2.get_details()
Computer(1,2,3).get_details()












































