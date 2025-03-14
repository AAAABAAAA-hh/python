class Monstor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #默认情况下,调用的是父类的 object 的__str__
    #要想直接输出对象信息 可以根据需要重写 __str__
    def __str__(self):
    # return super().__str__()
        return  f"{self.name} is {self.age} years old"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

m = Monstor ("青牛怪","200")
# 默认输出 类型和地址 十六进制 进行__str__方法重写后输出返回的信息
print(m)

# 输出十进制 地址
print(id(m))

#输出十六进制地址 对比
print(hex(id(m)))

#没有重写__eq__ 方法之前 == 比较的是内存地址
n = Monstor("青牛怪","200")
print(f"m == n:",{m == n})


























