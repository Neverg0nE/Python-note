#json data format
"""
{dict}
[{dict1},{dict2},{dict3}]
"""
import json                                           #When it comes to JSON conversion
data=[{'name':'gsq','age':19},{'name':'cry','age':19}]
data_json=json.dumps(data,ensure_ascii=False)          #convert the data to json,ensure_ascii=False can be ignored(no chinese)
print(data_json)

a_json="[{'name':'gsq','age':19},{'name':'cry','age':19}]"#if ' is internal," must be external
json.loads(a_json)                                     #convert the a_json to python format



#create a line chart using pycharts package
from pyecharts.options import TitleOpts, LegendOpts,ToolboxOpts,VisualMapOpts  #link with Line.set_global_opts()
from pyecharts.charts import Line  #import package
Line=Line()                                         #create a line chart object
Line.add_xaxis(['China','America','Uk'])            #add data of x-axis
Line.add_yaxis('GDP',[30,20,10])    #add data of y-axis

Line.set_global_opts(                               #set the global configuration. specific search:https://pyecharts.org/#/zh-cn/global_options
    title_opts=TitleOpts(title="GDP presentation",pos_left='center',pos_bottom='1%'),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
Line.render("basic line chart1.html")                                       #create picture,name the .html
#then there will create a render.html file in the left.Open it and click the browser.



#data handling 第一阶段第十章05，06