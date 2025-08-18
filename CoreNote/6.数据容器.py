# list
list=["gsq","ik",'cry',1314,True,["gsq","ik",'cry']]
a=list[-1][-1]            #This is how we can find the element from list of list.
b=list[0]                 #The first element from right to left is marked as -1,and the first element from right to left is marked as 0
list.index("gsq")         #find the subscript of elements
list[-1][1] = 'very ik'   #modify elements
list.insert(3,'4ever')  #insert elements
list.append('!')          #add elements method 1(for a single element)
list.extend(['!','!'])
list2=['!','!','!']
list.extend(list2)        #add elements method 2(for multiple element)
del list[4]               #delete elements method 1
list.pop(4)               #delete elements method 2 (4 means index)
extracted_element=list.pop(4)
print(extracted_element)  #mothod 2 can be extracted and output
list.count('!')           #count the number of element selected
len(list)                 #count  the number of all elements in the list
list.remove('!')          #delete the first element selected
while '!' in list:
    list.remove('!')      #use while to delete all element selected
list.clear()              #remove all elements from the list
print(list)

list=[1,2,3,4]

def list1():
    index = 0
    while index<len(list):
        print(list[index])
        index+=1
list1()

def list2():
    for x in list:
        print(x)
list2()

# Extract the even numbers from the list using while and for
list=[1]
x=2
while x<11:
    list.append(x)
    x+=1
print(list)

new_list1=[]
index=0
while index<len(list):
    x=list[index]
    if x%2==0:
        new_list1.append(x)
    index+=1
print(new_list1)

new_list2=[]
for x in list:
    if x%2==0:
        new_list2.append(x)
print(new_list2)

# tuple
from operator import index

t1 = (1, 'a', True, (1, 'a', True), 2)
t2 = ()  # empty tuple1
t3 = tuple()  # empty tuple2
t1[3][2]  # find elements
t1.index(2)  # find index
t1.count(True)  # count elements
len(t1)  # length

t4 = (1, 2, 3, 4, 5, [6, 7, 8, 9, 10])
index = 0
while index < len(t4):  # iterate through
    print(t4[index])
    index += 1
for x in t4:
    print(x)

t4[-1][-1] = 1  # modify list in tuple


# string
str="1314cry_ik_gsq1134"
str[4]                   #find elements by index
str.index('gsq')         #find the index of elements
a=str.replace('ik','veryik')      #replace elements(create a new string and can be received)
b=str.split('_')         #divide the string by special elements and convert it into a list
str.strip('14')          #remove the specified str before and after
str.count('_')           #count
len(str)                 #length

index=0
while index<len(str):
    print(str[index])
    index+=1
for x in str:
    print(x)


#sequence(list tuple string) and slice
list=[1,2,3,4,5,6,7,8,9]
tuple=(1,2,3,4,5,6,7,8,9)
string='123456789'
print(list[0:8:1])     #[starting index:ending index(exculding)
print(tuple[-1:0:-1])  #Not filling in means defaulting from the beginning to the end.Also for step
print(string[0:8:3])   #Negative means reverse execution

#set
set={1,2,3,4,5}    #no order and no repetition
set1={1,3,4,7}
set2={1,5,7}
set3=set()                     #define empty set
set.add(6)                     #add new elements
set.remove(6)                  #remove elements
set.pop()                      #pop elements randomly
set.clear()                    #clear set
set1.difference(set2)          #extract the elements that are in set1 but not in set2(create new set)
set1.difference_update(set2)   #delete the elements in set1 that are also in set2(no return,set1 is changed)
set1.union(set2)               #sum aggregate
len(set)                       #length
for x in set1:                 #iterate through
    print(x)


#dictionary
dict1={'gsq':100,'cry':99}    #Key:Value(key can't be dict)
dict2={}                      #def empty dict
dict3=dict()                  #define empty dict
print(dict1['gsq'])           #find value by key
dict0={'gsq':{"chinese":120,'math':150,'english':130},
       'cry':{"chinese":140,'math':140,'english':140},
       'jyy':{"chinese":150,'math':150,'english':150}}
print(dict0['gsq']['math'])   #find value in nested dict
dict0['gsq']['math']=122      #update value
dict0['gsq']['chemistry']=94  #add new key and value(same grammar)
print(dict0.pop('gsq'))       #delete specified key and can be output
len(dict0)                    #length
dict1.clear()                 #clear
dict0.keys()                  #get all keys in dict
for key in dict0.keys():
    print(key)
    print(dict0[key])         #iterate through by keys
for key in dict0:
    print(key)
    print(dict0[key])         #iterate through directly


#additional remarks
max(list)                     #find max elements(by ASCLL)
min(list)                     #find min elements(by ASCLL)
container=[1,2,3]
list(container)               #go list
str(container)                #go string
tuple(container)              #go tuple
set(container)                #go set
sorted(container)                   #sort in ascending order and turn it into a list
sorted(container,reverse=True)      #Reverse order, turn list


# use sort func to custom sorting
my_list=[["a",1],["b",3],["c",5]]
def choose_sort_key(x):
    return x[1]
my_list.sort(key=choose_sort_key,reverse=True)     #iterate through my_list and return every single element to the x when use sort func
print(my_list)

my_list.sort(key=lambda element:element[1],reverse=True)   #use lambda
print(my_list)