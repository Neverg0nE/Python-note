# open()function:
"""
open(name,mode,encoding)
name:str of object file(can include paths)
mode:'r':only reading;'w':only write,delete previous contents;'a':append
encoding:UTF-8
"""
import time
f=open('D:/临时安装包/4399.txt','r',encoding='UTF-8')
f.read(10)           #read 10 byte
f.read()             #read the full text
f.readlines()        #read all lines
f.readline()         #read one line once
for x in f:
    print(x)         #use 'for' to read every line
with open('D:/临时安装包/4399.txt','r',encoding='UTF-8') as f:
    for y in f:
        print(y)     #use with open can close the file automatically
time.sleep(10000)    #sleep 10000s(Occupying files)
f.close()            #Release the occupation and close the file

#tow method to count the number of 'it' in test.txt
f=open('D:/临时安装包/test1.txt','r',encoding='UTF-8')
content=f.read()
count=content.count('it')
print(f'the number of \'it\' in test1.txt is {count}')

n=0
for line in f:
    words=line.split()
    for word in words:
        if word=='it':
            n+=1
print(f'the number of \'it\' in test1.txt is {n}')
f.close()

# 'w' will create a new file and delete previous content,'a' will continue to write
import time
f=open('D:/临时安装包/test2.txt','w',encoding='UTF-8')
f.write("Hello world")              #write content into the fictitious file
f.flush()                           #write content to HD
time.sleep(100)
f.close()                           #include the function of flush()

f=open('D:/临时安装包/test2.txt','a',encoding='UTF-8')
f.write("Hello world")
f.write('\nnb')                       #\n let line feed
f.flush()
f.close()

#write the non-test data from f1 to f2
f1=open('D:/临时安装包/bill.txt','r',encoding='UTF-8')
f2=open('D:/临时安装包/bill.txt.bak','w',encoding='UTF-8')
for line in f1:
    line=line.strip()    #str*n
    turn_list=line.split(',')
    if turn_list[-1]=='测试':
        continue
    f2.write(line)
    f2.write('\n')
f1.close()
f2.close()