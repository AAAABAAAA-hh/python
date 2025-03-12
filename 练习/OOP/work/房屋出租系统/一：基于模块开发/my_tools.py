def read_confirm_select():
    while True:
        key = input("请输入你的选择(Y/N), 请确认选择:")
        if key.lower() == "y" or key.lower() == "n":
            break
    return key.lower()

def read_str(tip,default_val):
    str = input(tip)
    if len(str) > 0:
        return str
    else:
        return default_val





