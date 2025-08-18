from pymysql import Connection     # connection is a class
#连接
conn=Connection(                   # Establish a database connection
    host="localhost",              # hostname
    port=3306,                     # default
    user="root",
    password="2100"
)
print(conn.get_server_info())       # get 8.0.43(need code : mysql -uroot -p2100 to log in mysql firstly)


#创建表和其中的列
cursor=conn.cursor()                # ???获取对象
conn.select_db('cl')                # use database cl
cursor.execute('create table test_pymysql(id int)')   # create a table named test_pymysql and have an id-line
# 查找数据
conn.select_db('cl')
cursor.execute('select * from egr')
results=cursor.fetchall()
for row in results:
    print(row)                     # get every data in table egr
conn.close()                        # Close the database connection


# 添加数据到表中
"""
from pymysql import Connection
conn=Connection(                   
    host="localhost",              
    port=3306,                     
    user="root",
    password="2100",
    autocommit=True             # 自动提交，不用再写conn.commit()了
)
cursor=conn.cursor()
conn.select_db("cl")            # 选择库
cursor.execute("insert into egr values(7,'2000',20,'female')")    # 添加数据
conn.commit()                   # 提交
conn.close()                    #关闭

"""


# p138 Question








