# 闭包

# 简单闭包
def outer_func(logo):
     print("outer func")
     def inner_func(msg):
         print("inner func")
         print(f"{msg,logo} ")
     return inner_func

a=outer_func("python")    # 调用外部函数，返回内部函数的引用。
print(type(a))            # <type 'function'>
a("hello")                # 调用内部函数，传入参数。


# 内部修改外部函数变量
def outer(num1):
       def inner(num2):
            nonlocal  num1  # 修改外部函数的局部变量。
            num1+=num2
            print(num1)
       return inner

a=outer(5)    # num1=5
a(3)          # 输出8
a(4)          # 输出12


# 存取钱示例
def account_create(initial_balance=0):
    def atm(num,deposit=True):
        nonlocal initial_balance   # 非局部变量，修改外部函数的局部变量。
        if deposit:
            initial_balance+=num
            print(f"存款{num}元，当前余额为：",initial_balance)
        else:
            initial_balance-=num
            print(f"取款{num}元，当前余额为：", initial_balance)

    return atm
a=account_create()
a(100)
a(200)
a(50, False)


# 装饰器

# 装饰器的一般写法（闭包）
def sleep():
    import time
    import random
    print("睡眠中...")
    time.sleep(random.randint(1, 5))

def outer(func):
    def inner():
        print("我要睡觉了。")
        func()  # 输出：睡眠中... 然后随机睡眠1到5秒。
        print("我醒了！")

    return inner  # 返回闭包inner函数对象。

a = outer(sleep)  # 调用装饰器函数，传入要被装饰的函数sleep
a()  # 输出：我要睡觉了。 睡眠中... 我醒了！


# 装饰器的语法糖写法（@符号）
def outer(func):
    def inner():
        print("我要睡觉了。")
        func()
        print("我醒了！")

    return inner

@outer  # 将sleep作为参数传入到outer函数
def sleep():  # 等价于：a=outer(sleep)；a()
    import time
    import random
    print("睡眠中...")
    time.sleep(random.randint(1, 5))

sleep()  # 本质在调用inner函数