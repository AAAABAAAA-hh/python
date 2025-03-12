my_set = {"传智教育","黑马程序员","传智教育"}
my_set_empty = set()
print(my_set)
print(my_set_empty)
my_set.add("黑马")
print(my_set)

my_set = {"传智教育","黑马程序员","传智教育"}
my_set.clear()
print(my_set)

my_set = {"传智教育","黑马程序员","传智教育"}
my_set2 = {"传智教育","黑马程序员","传智教育","我是傻逼"}
set3 = my_set2.difference(my_set)
print(set3)
set3 = my_set.difference_update(my_set2)
print(set3)
