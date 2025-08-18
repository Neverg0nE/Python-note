#Basic
y=12
z=1                #给标识符赋值
print('x',y,z)     #变量可以直接用，连接
type(y)            #查看y的类型
int(5.5)           #转整数
float(y)           #转浮点
str(z)             #转字符串
e=input('hhh')     #input函数可以被接收为字符串，其内部内容会被print出来
a="cry"            #%表示占位，s表示将占位内容转化为字符串
b="ik"             #d转整数，f转浮点
c="gsq"            #占位内容可以是表达式
print("subject:"+a+" verb:%s"" object:%s"%(b,c))
d=a+b+c
print(d)           #字符串拼接
print('Ctrl+/')    #一键注释
print()            #输出一个换行
print("Hi",end='') #将两行print内容做成一行
print("World")     #''内空格数表示两个print内容之间的空格数
print('Hi\nworld') #Hi和world将分两行输出（换行操作）
print("Hi\tworld") #\t对齐两行print中的字词
print("is me \taaaa")


运算符="""          #三引号定义字符串，标识符可以是中文（英文，数字，下划线）
12/4               #除法运算
2**2               #指数运算
7//2               #除法取整数
3%2                #除法取余数
\                  #转义字符
"""

数字精度控制="""
m.n控制，m控制宽度（小于数字本身不生效），n控制精度，小数四舍五入
当宽度不足在数字前面补充空格，m和n均可省略
例：
%5f                #数字宽度为5
%.3f               #宽度不限，控制只有三位小数
"""
