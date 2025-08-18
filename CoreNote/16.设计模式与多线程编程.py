# 设计模式
from arrow.api import factory

# 单例模式 ：确保一个类只有一个实例，并提供一个全局访问点。
# 工厂模式 ：定义一个创建对象的接口，但由子类决定要实例化的类是哪一个。工厂方法让类的实例化推迟到子类。

class Person:
    pass
class Worker(Person):
    pass
class Manager(Person):
    pass
class Student(Person):
    pass
class Factory:
    def get_person(self, p_type):
        if p_type == "w":
            return Worker()
        elif p_type == "m":
            return Manager()
        else:
            return Student()
fac=Factory()
worker=fac.get_person("w")
manage=fac.get_person("m")
stu=fac.get_person("s")

# 多线程编程
import time
import threading


def sing(msg):
    while True:
        print("正在唱:", msg)
        time.sleep(1)


def dance(d_type):
    while True:
        print("正在跳:", d_type)
        time.sleep(2)


def rap():
    while True:
        print("正在Rap...")
        time.sleep(3)


def basketball():
    while True:
        print("正在打篮球...")
        time.sleep(4)


if __name__ == '__main__':
    # sing()
    # dance()                 #  多个函数无法同时执行,只有第一个sing()在执行

    # 创建线程对象,target:指定要执行的函数名, args: 元组方式传参，kwargs: 字典方式传参
    sing_thread = threading.Thread(target=sing, args=("只因你太美",))  # 创建一个唱歌线程，目标函数为sing，没有逗号就不算元组
    dance_thread = threading.Thread(target=dance, kwargs={"d_type": "铁山靠"})  # 创建一个跳舞线程，目标函数为dance
    rap_thread = threading.Thread(target=rap)  # 创建一个跳舞线程，目标函数为rap
    basketball_thread = threading.Thread(target=basketball)  # 创建一个跳舞线程，目标函数为basketball

    sing_thread.start()
    dance_thread.start()
    rap_thread.start()
    basketball_thread.start()  # 启动所有线程