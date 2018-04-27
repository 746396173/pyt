#c/s架构  客户端服务器架构
#b/s架构  浏览
from socket import *
import struct
import sys

udpsocket = socket(AF_INET,SOCK_DGRAM)

cmd_buf = struct.pack("H8sb5sb",1,"test.jpg",0,"octet",0)

sendAddr = ("192.168.0.102",69)

udpsocket.sendto(cmd_buf,sendAddr)

p_num = 0
recvFile = ""

while True:
    recvData,recvAddr = udpsocket.recvfrom(1024)

    recvDataLen = len(recvData)

    cmdTuple = struct.unpack("HH",recvDate[:4])

    cmd = cmdTuple[0]
    currentPackNum = cmdTuple[1]

    if cmd == 3:
        if currentPackNum == 1:
            recvFile = open("test.jpg","a")

        if p_num + 1 == currentPackNum:
            recvFile.write(recvData[4:]);
            p_num += 1
            print('(%d)次接收到的数据' % (p_num))

            ackBuf = struct.pack("!HH", 4, p_num)

            udpsocket.sendto(ackBuf, recvAddr)
            # 如果收到的数据小于516则认为出错
        if recvDataLen < 516:
            recvFile.close()
            print('已经成功下载！！！')
            break

        elif cmd == 5:  # 是否为错误应答
            print("error num:%d" % currentPackNum)
            break

udpsocket.close()
