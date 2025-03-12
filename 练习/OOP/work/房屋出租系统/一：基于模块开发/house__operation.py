from cmath import phase
from pdb import find_function
from random import choice

from my_tools import *

def main_menu():
    #显示主菜单 和 退出功能
    print("房屋出租系统菜单".center(30, "="))
    print("\t\t\t1 新 增 房 源")
    print("\t\t\t2 查 找 房 屋")
    print("\t\t\t3 删 除 房 屋 信 息")
    print("\t\t\t4 修 改 房 屋 信 息")
    print("\t\t\t5 房 屋 列 表")
    print("\t\t\t6 退 出")

#全局变量 houses
houses = [{"id":1,"name":"tim","phone":113,"address":"海淀","rent":800,"state":"未出租"}]


def list_houses():
    """
    显示房屋信息
    :return:
    """
    print("房屋列表".center(60, "="))
    print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(未出租/已出租)")
    for house in houses:
        for value in house.values():
            print(value, end="\t\t")
        print()
    print("房屋列表显示完毕".center(60, "="))

#全局变量 id_counter 记录当前房屋的id号
id_counter = 1

def add_house():
    #完成添加房屋信息
    print("添加房屋".center(60, "="))
    name = input("姓名：")
    phone = input("电话：")
    address = input("地址：")
    rent = int(input("租金："))
    state = input("状态")
    global id_counter
    id_counter += 1
    #构建字典加入全局house
    house ={"id":id_counter,"name":name,"phone":phone,"address":address,"rent":rent,"state":state}
    houses.append(house)
    print("添加房屋成功".center(60, "="))

def del_house():
    print("删除反诬信息".center(60, "="))
    def_id = int(input("请输入删除房屋的编号(-1退出)："))
    if def_id == -1:
        print("放弃删除房屋信息".center(60, "="))
        return
    #确认删除
    choice = read_confirm_select()
    if choice == 'y':
        house = find_by_id(def_id)
        if house:
            houses.remove(house)
            print("删除房屋信息成功".center(60, "="))
        else:
            print("房屋编号不存在，删除失败")
    else:
        print("放弃删除房屋信息".center(60, "="))

def find_by_id(find_id):
    for house in houses:
        if house["id"] == find_id:
            return house
    return None

def edit_sys():
    print("请输入你的选择(Y/N):")
    choice = read_confirm_select()
    if choice == 'y':
        return True
    else:
        return False

def find_house():
    print("查找房屋信息".center(60, "="))
    find_id = int(input("请输入要查找哦的id: "))
    house = find_by_id(find_id)
    if house:
        print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(未出租/已出租)")
        for value in house.values():
            print(value, end="\t\t")
            print()
    else:
        print(f"查找房屋id: {find_id}不存在")

def update_house():
    update_id = int("请选择待修改的房屋编号(-1表示退出)：")
    if update_id == -1:
        print("你放弃修改房屋".center(60, "="))
        return
    house = find_by_id(update_id)
    if  not house:
        print("没有要修改的房屋信息".center(60, "="))
        return
    name = input(f"姓名{house["name"]}")
    if  not name:
        house["name"] = name
    phone = input(f"电话号码{house["phone"]}")
    if not phone:
        house["phone"] = int(phone)
    address = input(f"地址{house["address"]}")
    if not address:
        house["address"] = address
    rent = input(f"租金{house["rent"]}")
    if not rent:
        house["rent"] = int(rent)
    state = input(f"状态{house["state"]}")
    if not state:
        house["state"] = state
    print("修改房屋信息成功".center(60, "="))









































































