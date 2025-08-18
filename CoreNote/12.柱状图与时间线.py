#creat bar chart
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
bar=Bar()                                        #create bar chart object
bar.add_xaxis(["China","America","UK"])          #create x-axis
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right")) #create y-axis，thh code after“，” is aims to set up the position of data
bar.reversal_axis()                             #reverse the x-axis and y-axis
bar.render("basic bar chart1.html")             #create bar chart

#Timeline
from pyecharts.charts import Bar,Timeline  #leading-in package timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType    #change colour

bar1=Bar()
bar1.add_xaxis(["China","America","UK"])
bar1.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2=Bar()
bar2.add_xaxis(["China","America","UK"])
bar2.add_yaxis("GDP",[50,30,40],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3=Bar()
bar3.add_xaxis(["China","America","UK"])
bar3.add_yaxis("GDP",[70,50,60],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

timeline=Timeline({"theme":ThemeType.LIGHT})                      #create timeline object,and how to set up theme(colour)
timeline.add(bar1,"point1")                              #add bar chart object in timeline
timeline.add(bar2,"point2")
timeline.add(bar3,"point3")

timeline.add_schema(
    play_interval=1000                                            #set up the speed of play timeline,unit:ms
)
timeline.render("basic timeline of bar chart.html")


#Development of dynamic GDP bar chart P110 第一阶段第十二章03