# 处理数据
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts

# 打开文件
f_us = open("D:/date\美国.txt","r",encoding="utf-8")
# 去掉不规范的json格式
us_data = f_us.read()
us_data = us_data.replace("jsonp_1629344292311_69436("," ")
us_data = us_data[:-2]
# json转python字典
us_dict = json.loads(us_data)
# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
# 取日期数据，用于x轴，取2020年，到315下标结束
us_x_data = us_trend_data['updateDate'][:314]
# 获取y轴数据
us_y_data = us_trend_data['list'][0]['data']
# 生成图表
line = Line()
# 构建折线图的x轴和y轴  以及折线图
line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊数据",us_y_data)
# 全局系统配置仅以title引例，其他不再书写，如需寻找可在网站或基础折线图中查看
line.set_global_opts(
    title_opts = TitleOpts(title="2020美国确诊人数对比折线图", pos_top="None", pos_bottom="5%", pos_left="True"),
)

line.render("us_fection_data.html")
# 关闭文件
f_us.close()












