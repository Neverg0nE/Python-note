#Bool and if

#Bool
比较运算符="""           #通过比较运算符计算得到布尔类型的结果True或False
==                      #判断内容是否相等
!=                      #判断内容是否不等
>
<
>=
<=
"""



#if
"""
if 条件1：
    满足条1 做1
    满足条1 做2
    if 条件2：
        满足条2 做1
        满足条2 做2
elif 条件3：          #当条件1不满足的时候进入到elif判断条件3
    满足条件3 做3
elif 条件N：          #若上一个elif满足此elif不进行判断
    满足条件N 做N
只有满足第一个if才会执行第二个if
else:
    条件4（当if不满足执行此条）
"""


#例题1
height=1130
level=5
print("欢迎来到动物园")
if height>120:
    print("你的身高不符合免费的要求")
    if level>3:
        print("但由于你的VIP等级较高，你可以免费游玩")
    else:
        print("且VIP等级不高，你需要补票")
else:
    print("你可以免费游玩")



#例题2
print('公司将要发礼物了')
if 18<=int(input("请输入你的年龄："))<30:
    print("你的年龄达标了。")                            #前置条件
    if int(input("请输入你的入职时间：(单位：年)"))>2 :
        print("你有获取礼物的资格，恭喜你！")
    elif int(input("请输入你的级别："))>3 :              #或
        print("你有获取礼物的资格，恭喜你！")
    else:
        print('尽管年龄够了，入职时间和级别都不满足，你无法得到礼物')
else :
    print('你的年龄不满足条件，你不满足得到礼物')



# 例题3
import random
num=random.randint(1,10)          #产生随机数字
print('这是一个猜数字游戏，请从1-10里面选出我心中所想的数字，'
      '你总共有3次机会尽可能的用最短的次数猜中我想的数字吧！')
guess_num=int(input("输入你猜的数字吧："))
if  guess_num==num:
    print('恭喜你第一次就猜对了')
else:
    if guess_num<num:
        print('偏小了往大的猜')
    else :
        print('偏大了往小的猜')
    guess_num=int(input("输入你第二次猜的数字吧："))
    if  guess_num==num:
        print('恭喜你第二次就猜对了')
    else:
        if guess_num<num:
            print('偏小了往大的猜')
        else :
            print('偏大了往小的猜')
        guess_num = int(input("输入你第三次猜的数字吧："))
        if guess_num == num:
            print('恭喜你把握住了最后一次机会猜对了')
        else:
            print('你没有机会了，正确答案是:',num)


