# Account类 姓名 余额 密码
# set__xxx 赋值
# query__info 接收姓名和密码

class Account:
    __name = None
    __account = None
    __password = None

    def set__xxx(self, __name, __account, __password):
        if 4 >= len(str(__name)) >= 2:
            self.__name = __name
        else:
            print("输入信息不符合规定，默认名称为 111")
            self.__name = "111"
        if __account >= 20:
            self.__account = __account
        else:
            print("输入信息不符合规定")
            self.__account = 0
        if len(str(__password)) == 6:
            self.__password = __password
        else:
            print("输入信息不符合规定，默认密码为 000000")
            self.__password = 000000

    def query__info(self, __name, __account, __password):
        if __name == self.__name and __password == self.__password:
            return self.__account
        else:
            print("账号或密码错误，请重新输入。")


ming = Account()
ming.set__xxx("明", 123456, 122211)






















