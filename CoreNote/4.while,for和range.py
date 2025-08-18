#while for and range

# while循环语句
"""
while 条件1：
    条件1满足时，做1
    条件1满足时，做2
    条件1满足时，做3
    while 条件2：
        条件2满足时，做1
        条件2满足时，做2
1.条件为bool类型，True继续False终止
2.设置终止条件
"""

# for循坏语句
"""
for 临时变量 in 待处理数据集:
    循环满足条件执行的代码
"""

# Range
"""
range(num)
获取一个从0开始，到num结束的数字序列（不包含num本身）
语法一：如range（5）取得数据[0,1,2,3,4]
语法二：range（num1，num2），取得num1开始到num2结束的数字序列（不包括num2本身）
语法三：range（num1，num2，step），step定义步长，默认为1；如rage（5，10，2），取得数据[5,7,9]
"""

# for
"""
For：
for 临时变量 in 待处理数据集:
循环满足条件执行的代码
"""

# continue and break
"""
continue:中断本次循环直接进入下一次循环
break:遇到break结束循环
"""


# 例题1：100个6
i=0
while i<100:
    print('6')
    i+=1



# 例题2：1~100的和计算
a=1
b=0
while a<=100:
    b+=a
    a+=1
print(f'1~100累加的和是：{b}')


# 例题3：无限次猜数字游戏播报猜测次数
import random
num=random.randint(1,100)
print(num)
print('这是一个猜数字游戏，你需要从1~100中猜中我心里想的那个数字，你有'
      '无限次机会，最后我会告诉你你猜了几次')
guess_num=int(input("请输入你猜的数字:"))          #易错点
b=True
count=0
while b:
    guess_num = int(input("请输入你猜的数字:"))
    count+=1
    if num==guess_num:
        print("你猜对了")
        b=False
    else:
        if num>guess_num:
            print('你猜的偏小了')
        else:
            print('你猜的偏大了')
print(f'你总共猜测了{count}次')


# 例题4：while嵌套的运用，一共七天每天三顿饭
i=1
while i<=7:
    print(f'今天是第{i}天')
    i+=1
    j=1
    while j<=3:
        print(f'吃的第{j}顿饭')
        j+=1
print(f"一共吃了{i-1}天饭")


# 例题5：while嵌套的运用，九九乘法表
i=1
while i<=9:
    j=1
    while j<=i:
        print(f'{j}*{i}={j*i}\t',end='')
        j+=1
    i+=1
    print()
# 实战结果：
a=1
b=1
# a*b
while a<=9:
    a=1
    while a<=b:
        print(f'{a}*{b}={a*b}\t',end=' ')
        a+=1
    b+=1
    print()


#for的基础操作
willing="ikcry"         # 依次取出
for x in willing:
    print(x)


#例题6：for的运用，计算句子中a的数量
name="i want to stay with cry forever"
num=0
for x in name:
    if x=="a" :
        num+=1
print(f"被统计的字符串中有{num}个a")

# 例题7：for for嵌套循环
x=1
y=1
for x in range(1,4):
    print(f"今天是我吃饭的第{x}天")
    for y in range(1,3):
        print(f"今天是我吃的第{y}顿饭")



#输出0，1，2，3，4
for x in range(5):
    print(x)



# 得到四个"ikcry"
for x in range(2,10,2):
    print("ikcry")



# 计算1~100的偶数个数（或令step为2）
num=0
for x in range(1,100):
    if x%2==0:
        num+=1
print(f"There are {num} even number in range 1~100")



# Multiplication Table of 9x9
for i in range(1,10):
    for j in range(1,1+i):
        print(f'{i}*{j}={i*j}\t',end='')
    print()   #Export CR(Carriage Return)



# Application of for,range,continue,break and if
Total=10000
m=1
for n in range(0,21):
    import random
    num = random.randint(1, 10)
    n+=1
    if num<5:
        print(f'Employee{n} gets {num} points.No payment will be made for a point below 5.Next one')
        continue
    else:
        print(f'Employee{n} gets {num} points.Received a salary of 1,000 yuan, with an account balance of {10000-m*1000} yuan.')
        m+=1
        if m==11:
            print('The salary has been paid out. Please come to collect it next month.')
            break