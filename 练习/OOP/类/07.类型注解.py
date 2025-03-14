# 变量类型注解
n1: int = 10
n4 = 10  # type: int
n2: float = 20
is_pass: bool = True
name: str = "str"


# 实例对象类型注解  对cat 进行注解 表明类的类型
class Cat:
    pass


cat: Cat = Cat()
# 容器类型注解
my_list: list = [1, 2, 3, 4, 5]
my_tuple: tuple = (1, 2, 3, 4, 5)
# 容器详细类型注解
my_list1: list[int] = [1, 2, 3, 4, 5]
my_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3}


# 函数的类型注解
def func1(name: str) -> None:
    print(name)


# Union 类型
from typing import Union

a: Union[int, str] = 100
list1: list[int | str] = [1, 2, 3, 4, 5, "ming"]
list2: list[Union[int,str]] = [1, 2, 3, 4, 5, "ming"]
def func2(name: Union[int ,str]) -> None:
    pass

    

