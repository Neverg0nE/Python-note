#Visual map
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
from pyecharts.options import *
my_map=Map()                             #prepare the map target
data=[                                #prepare the data
    ("北京市",99),
    ("上海市",199),
    ("湖南省",299),
    ("台湾省",399),
    ("广东省",499),
    ("江苏省",400)
]
my_map.add("test map",data,"china")      #add data

my_map.set_global_opts(                                     #set the global configuration
    title_opts=TitleOpts(title="Province"),                 #set the title(leading-in package)
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,                                  #设置分段，3段
        pieces=[
            {'min':1,"max":9,"label":"1-9","color":'#CCFFFF'},           #AB173,前端，rgb颜色对照表获取颜色代码
            {'min':10,"max":99,"label":"10-99","color":'#FF6666'},
            {'min':100,"max":500,"label":"100-500","color":'#990033'}
        ]
    )
)
my_map.render("china map.html")


#data handling and make other visual map 第一阶段第十一章02，03