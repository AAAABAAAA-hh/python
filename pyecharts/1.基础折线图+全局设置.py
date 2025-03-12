# 导入pyecharts 包直达line
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, VisualMapOpts, TooltipOpts, ToolboxOpts

# 得到折线图对象
line  = Line()
# 添加折线图数据
line.add_xaxis(["中国","美国","英国","法国"])
line.add_yaxis("GDP",[60,30,40,30])
# 通过全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title = "GDP展示",pos_left="center",pos_bottom="1%"),
    legend_opts= LegendOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True)
)
line.render("practice1.html")











