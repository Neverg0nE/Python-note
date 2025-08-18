# Socket服务端开发,配合netAssist.exe使用，或Socket客户端
import socket
socket_server=socket.socket()             # 创建一个socket对象
socket_server.bind(('localhost',8000))    # 绑定地址(本机）和端口（8000）
socket_server.listen(5)                   # 监听连接，最大连接数为5
result:tuple=socket_server.accept()       # 接受客户端连接，返回一个新的socket对象和客户端地址,得到二元元组，如下两行代码
print("等待客户端连接...")                  # accept()为阻塞方法，没链接不向下执行
coon=result[0]                            # 客户端和服务端的连接对象
address=result[1]                         # 输出客户端地址信息
print(f"已连接的客户端地址：{address}")       # 提示已连接的客户端地址信息
while True:
    data=coon.recv(1024).decode('UTF-8')      # 接收数据，最大接收1024字节;后面的.decode('UTF-8')是将接收到的二进制数据解码为字符串。
    print(f"接收到来自{address}的数据：{data}")  # 输出接收到的数据data
    msg=input("请输入要发送给客户端的消息：")
    if msg == "exit":
        break                             # 如果发送的消息是"exit"，则退出循环
    coon.send(msg.encode('UTF-8'))        # 将输入的字符串编码为二进制数据,发送数据给客户端
coon.close()                              # 关闭连接对象
socket_server.close()                     # 关闭服务端socket对象



# Socket客户端开发
import socket                                            # 导入socket模块
socket_client=socket.socket()                            # 创建一个socket对象
socket_client.connect(('localhost',8000))                # 连接到服务器，指定IP地址和端口号
while True:                                              # 循环发送消息到服务器，直到手动退出循环
    msg=input('请输入给服务器发送的消息: ')
    if msg =="exit":
        break
    socket_client.send(msg.encode("UTF-8"))              # 发送数据到服务器
    data = socket_client.recv(1024)                      # 接收服务器返回的数据
    print(f"服务端回复的消息是{data.decode('UTF-8')}")      # 打印接收到的数据

socket_client.close()                                    # 关闭连接