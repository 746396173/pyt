#coding=utf-8

from socket import *

#1. 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#2. 绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
bindAddr = ('', 7788) # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udpSocket.bind(bindAddr)

#3. 等待接收对方发送的数据
recvData = udpSocket.recvfrom(1024) # 1024表示本次接收的最大字节数

#4. 显示接收到的数据
print (recvData)#网络调试助手发送的数据包为一个元祖(数据,(地址,端口))
print(recvData[0].decode("utf-8"))
#5. 关闭套接字
udpSocket.close()