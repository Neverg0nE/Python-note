#functions return multiple values
def test_return():
    return 1,'hello',True
x,y,z=test_return()
print(x,y,z)


#parameters passing
def per_info(name,age,gender='male'):
    print(f'your name is:{name},your age is {age},your gender is {gender}')
    return                                    #default man(empty gender=male)(must set the default value at the end)
per_info('gsq',19,'male')    #ponsitional parameters passing(be ordered)
per_info(name='gsq',age=19,gender='male')     #keyword argument(can be unordered)
per_info('gsq',gender='male',age=19)    #interchangeable(positional para must before kw args)
per_info('cry' ,19,'female') #change the gender
#for parameters whose number is unknown
def user_info1(*args):                        #positional parameters passing get tuple
    print(args)
user_info1(19,'gsq',True)
user_info1(True,18)
def user_info2(**kwargs):                     #kwyword arguments get dict
    print(kwargs)
user_info2(name='gsq',age=19,gender='male')
user_info2(age=18)

#let func as parameters and lambda temporary func
def out_func(in_function):
    result=in_function(1,2,3)
    print(result)
def in_function(x,y,z):
    return x+y*z
out_func(in_function)
out_func(lambda x,y,z:x+y+z)       #define anonymous and temporary func which can't be reused