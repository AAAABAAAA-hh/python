# 提供各种操作
from house__operation import *
def main():
    #调用函数 main_menu 显示主菜单
    while True:
        main_menu()
        key = input("请输入你的选择(1-6)")
        if key in ["1","2","3","4","5","6"]:
            if key == "1":
                add_house()
            elif key == "2":
                find_house()
            elif key == "3":
                del_house()
            elif key == "4":
                update_house()
            elif key == "5":
                list_houses()
            elif key == "6":
                if edit_sys():
                    print("你退出了系统，欢迎下次使用。。。。。。")
                break

            else:
                print("你输入的序号不对,请重新输入：")

if __name__ == "__main__":
    main()
    list_houses()

