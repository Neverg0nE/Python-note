# catch exception
"""
try:
    abnormal code may occur
except:                      #capture all error(can be writen as except Exception as e:)
    If there is code that executes abnormally
else:
    run the code(when there is no error)
finally:
    run the code(perform regardless of exceptions)
"""
import try_package.file_util

try:
    print(cry)               #name is undefined
except NameError as e:       #capture a NameError(as e can be omitted)
    print('occur NameError')
    print(e)

try:
    print(1/0)
except(NameError,ZeroDivisionError) as e: #capture multiple error
    print(e)


#Module模块
"""
[from 模块名] import [模块|类|变量|函数|*][as 别名]
1.
import.模块名
import.模块名1，模块名2
模块名.功能名（）
2.
from 模块名 import 功能名
功能名（）
3.from 功能名 import *   # * means all
功能名
4.模块定义别名
import 模块名 as 别名
5.功能定义别名
from 模块名 import 功能 as 别名

"""
#1.
# import time     #import the built-in time module(time.py),ctrl+left click time get source code
# print('hello')
# time.sleep(5)   #time.xxx can use all function of time.py
# print('hello world')
#2.
# from time import sleep
# print('Hello')
# sleep(5)
# print('Hello world')
#3.
# from time import *
# print('Hello')
# sleep(5)
# print('Hello world')
#4.
# import time as t
# t.sleep(2)
# print("hello")
#5.
# from time import sleep as sl
# sl(2)
# print('hello')



#self-developed module (This part needs to be used together with my_package)

# import my_package.my_module1
# my_package.my_module1.add(1,2)

# from my_package.my_module1 import add
# add(1,2)

# from my_package.my_module1 import *     # *=__all__.If * is redefined in module,other func will not be used
# add(1,2)
# divi(2,4)
# mul(3,54)



#python package(This part needs to be used together with my_package)

# import my_package.my_module1           #the complete writing
# import my_package.my_module2
# my_package.my_module1.add(1,4)
# my_package.my_module2.prt()

# from my_package import my_module1      #invoking func should not write my_package
# from my_package import my_module2      #becase use import module
# my_module1.add(1,4)
# my_module2.prt()

# from my_package.my_module1 import add    #only invoke func in module
# from my_package.my_module2 import prt
# add(1,4)
# prt()


#install third-party package
"""
1.win+CMD
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple third-party package name
check method:
enter python in CMD
enter import third-party package name

2.click lower right corner
interpreter settings
click +
search third-party package name
click option and write -i https://pypi.tuna.tsinghua.edu.cn/simple to accelerate
install
"""


#try_package
from try_package import str_util
from try_package import file_util
print(str_util.str_reverse('asdawdasdasda'))
print(str_util.substr('askdjhakwjd',0,5))
file_util.append_to_file('D:/临时安装包/4399.txt','123')
file_util.print_file_info('D:/临时安装包/4399.txt')