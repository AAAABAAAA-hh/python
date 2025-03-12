"""
    构建一个记录登记信息的文件
    仅写功能函数
    不再进行 main 的创建---无限循环
    直接写文件名称，默认将文件创建在当前py文件之下
"""

import datetime

def operation_menu():
    print("请选择操作".center(32,"="))
    print("\t\t\t查看当前登录用户")
    print("\t\t\t查看登录日志")
    print("\t\t\t退出系统")

def record_log(user,info):
    """
    记录登录信息
    :param user:当前登录用户 
    :param info: 当前登录失败或成功的信息
    :return:   
    """
    with open("log.txt","a",encoding = "utf-8") as f:
        s = f"登录用户{user}，登录状态：{info},登录时间:{datetime.datetime}\n"
        f.write(s)

def read_log():
    with open("log.txt","r",encoding = "utf-8") as f:
        for line in f:
            print(line)

#测试
if __name__ == '__main__':
    user = input("请输入用户名：")
    pwd = input("请输入密码：")

    if user.lower() in ["smith","tom","hsp"] and pwd == "8888" :
        record_log(user,"登录成功")
    else:
        print("用户名或密码错误，请重新输入。")






































