# Design a class
class Student:         # Define a class named Student
    name=None          # The attributes of the class:Member variables
    age=None

    def say_hi(self):  # The behavior of the class:Member method
            print(f"Hi, my name is {self.name}","I am "+str(self.age)+" years old.")  # use self to access the attributes of the class
    def reply(self,msg):
            print(f'my name is {self.name}',msg)

stu=Student()          # Create an object named stu
stu.name="gsq"         # Assign values to the object's properties
stu.age=20
stu.say_hi()           # Call the object's methods

stu2=Student()
stu2.name="cry"
stu2.age=19
stu2.reply("and nice to meet you!") # Call the object's methods and pass a parameter

print(stu.name)        # Print the values of the object's properties


# Constructor __init__
class Person:
    name=None
    age=None
    tel=None            #when use __init__ method, it can be ignored
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel    #creat member variable
        print('Person class created a class object')

stu=Person('John',20,'010-1234-5678')   #execute __init__ method automatically
print(stu.name)
print(stu.age)
print(stu.tel)


#Magic method
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):                # Magic method:__str__
        return f"Student class object,name:{self.name},age{self.age}"

    def __lt__(self, other):          # Magic method:__lt__(< or >)
        return self.age < other.age

    def __le__(self, other):          # Magic method:__le__(<= or >=)
        return self.age <= other.age

    def __eq__(self, other):          # Magic method:__eq__(== or !=)
        return self.age == other.age

stu1=Student("gsq",20)
stu2=Student("cry",19)
print(stu1)                           # __str__
print(stu1 < stu2)                    # __lt__
print(stu1 <= stu2)                   # __le__
print(stu1 == stu2)                   # __eq__


# Encapsulation
class Phone:
    __current_voltage = 0.5  # private member variable,0.5 can be changed to 1

    def __keep_single_core(self):  # private method
        print("CPU is working in just single-core operation")

    def call_by_5g(self):
        if self.__current_voltage >= 1:  # private variable can be used in class
            print("5g is opened")
        else:
            self.__keep_single_core()  # private method can be used in class too
            print("5g is not opened because your phone is in low voltage")


phone = Phone()  # create an object
phone.__current_voltage = 1  # can not be changed because it is private variable
phone.call_by_5g()  # can be called because it is public method
phone.__keep_single_core()  # error because private method
print(phone.__current_voltage)  # error because private variable



#Inheritance
"""
class class_name(parent_class_name):
    new methods and attributes
"""
class Phone2020:
    IMEI:None
    productor="HUAWEI"
    def call_by_4g(self):
        print("Calling by 4g")

class Phone2021:
    face_id="Yes"
    def call_by_5g(self):
        print("Calling by 5g")

class Phone2022(Phone2020,Phone2021):  # Inheritance from Phone2020 and Phone2021
    pass                               # No new methods and attributes
                                       # If there exit same methods or attributes in parent classes, the first one will be used
phone=Phone2022()
print(phone.productor)
print(phone.face_id)
phone.call_by_4g()
phone.call_by_5g()



# Override
class IPhone:
    producer="Apple"
    def call_by_5g(self):
        print("5G!!!")
class IPhone7(IPhone):
    producer = "HUAWEI"                                    # override the producer
    def call_by_5g(self):                                  # override the method
        print("5G.")
    print(f"The producer of IPhone is {IPhone.producer}")  # lead parent class in the child class
    IPhone.call_by_5g(IPhone)                              # call the method in the parent class

phone=IPhone7()
print(phone.producer)



# type annotation for variables
from typing import Union
"""
1.var: type = value
2.var= value # type: type
3.def function(var: type): -> return_type
    pass
4.Union[type1, type2]  # use Union package
"""
a: int = 10
class Student:
    pass
b: Student = Student()      # e is an object of Student class
c: list = [1, 2, 3]
d: list[int] =[1,2,3]       # more specific type annotation for list
e: tuple[int, str] = (1, "Hello")
f: dict[str, int] = {'a': 1, 'b': 2}
g = 10                      # type:int     # type annotation using comment
h = Student()               # type:Student
def add(x: int, y: int) -> int:  # type annotation for function and return type
    return x + y
i:list[Union[str,int]]=[1,2,"CRY"]
j:dict[str,Union[int,str]]={"a":1,"b":"CRY"}
def function(var: Union[int, str]) ->Union[int, str]: # type annotation for function
    pass



# Polymorphism
class Animal:                # Abstract class
    def speak(self):         # Abstract method(only pass)
        pass

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

def make_noise(animal:Animal):      # the type of animal is Animal(class)
    animal.speak()                  # the type of animal is Dog or Cat

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


#Big Question : P124-P126