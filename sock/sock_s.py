import socket   #socket模块
import subprocess   #执行系统命令模块
HOST=''
PORT=8083

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP
s.bind((HOST,PORT))   #套接字绑定的IP与端口
s.listen(5)         #开始TCP监听


while True:
    print('waiting for connection...')
    c,addr=s.accept()   #接受TCP连接，并返回新的套接字与IP地址
    print('Connected by',addr)   #输出客户端的IP地址
    while True:
        data=c.recv(1024)    #把接收的数据实例化
        print(data.decode(encoding='utf-8'))
        c.sendall("收到".encode(encoding='utf-8'))


conn.close()     #关闭连接