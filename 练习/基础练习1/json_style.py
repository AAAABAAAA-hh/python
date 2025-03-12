#导入json格式
import json
#定义一个json格式要求的python数据
practise = [{"1":10,"2":"老王"},{"3":100,"4":"老马"}]
#通过json.dump（practise）方法把python数据转换为json数据
practise = json.dumps(practise)
print(practise)
#通过json.loads(practise)将json格式转化为pyhton数据
practise = json.loads(practise)
print(practise)

#json方法通过dumps方法将python格式转化为json格式
#





