#Function
"""
def func_name（parameters）：
    function
    return returned_value
"""
# Calculator
def calculator(x,y):
    """
    The cal function is used to calculate the product of two numbers
    :param x: the first number to multiply
    :param y: the second number to multiply
    :return: the product of two numbers
    """
    result=x*y
    print(f'{x}*{y}={result}')
    return
calculator(2,1)


#Use a function to determine whether an age is eligible to enter an internet café.
def inter_bar(x):
    if x>18:
        return True
    else:
        return

result=inter_bar(17)

if result:
    print('Welcome to our internet bar')
if not result:
    print('Your age is under 18 years old,so you cannot enter our internet bar')


# The usage of global variables
num=2100
def a():
    print(num)
    return
def b():
    global num
    num=2000
    print(num)

a()
b()
print(num)


#Bank storage system
from random import choice
money=100
def main():
    print('----------Main Menu----------')
    global name
    name=input('Please enter your name here:')
    print(f'{name},Welcome to 2100 ATM,please choose the service you want here:')
    print('Check the balance\t[Enter 1]')
    print('Deposit\t\t\t\t[Enter 2]')
    print('Draw\t\t\t\t[Enter 3]')
    print('Exit\t\t\t\t[Enter 4]')
    global choice
    choice=int(input('Please enter your choice here:'))

def CK(x):
    if x:
        print('----------Balance inquiry----------')
    print(f'Hello {name},your balance is:{money}yuan')
    return

def DP():
        print('----------Deposit----------')
        num = int(input('Enter the amount you want to deposit:'))
        global money
        money+=num
        print(f'Hello {name},you deposit {num}yuan successfully')
        CK(False)
        return

def Draw():
    print('----------Draw----------')
    num = int(input('Enter the amount you want to draw:'))
    global money
    money-=num
    print(f'Hello {name},you withdraw {num}yuan from your account successfully')
    CK(False)

while True:
    main()
    if choice==1:
        CK(True)
        act=input('Press any key to return to the main menu:')
        continue
    if choice==2:
        DP()
        act = input('Press any key to return to the main menu:')
        continue
    if choice==3:
        Draw()
        act = input('Press any key to return to the main menu:')
        continue
    if choice==4:
        print('Welcome back next time')
        break


