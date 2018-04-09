import re
import time
import socket
import threading
from struct import pack, unpack
MESSAGE_TYPE_FROM_CLIENT = 689
MESSAGE_TYPE_FROM_SERVER = 690
#	创建socket
#tcpClientSocket	= socket(AF_INET,SOCK_STREAM)
#	链接服务器
serAddr	= ('openbarrage.douyutv.com',8601)
tcpClientSocket= socket.create_connection(serAddr)
#time.sleep(5)
print("socket信息"+str(tcpClientSocket))
message_body = b'type@=loginreq/roomid@=122402/\0'#转义后要发送的 数据部分字符串必须是二进制的
msg_type = MESSAGE_TYPE_FROM_CLIENT
mss = pack('<llhbb%ds'%(len(message_body)), len(message_body)+8, len(message_body)+8, msg_type, 0, 0, message_body)#打包成二进制流
tcpClientSocket.send(mss)#发送
#	接收对⽅发送过来的数据，最⼤接收1024个字节
recvData = tcpClientSocket.recv(4096)#收到的是二进制流
print("服务器返回值1"+str(recvData))
join = b"type@=joingroup/rid@=122402/gid@=-9999/\0"
#msg_type = MESSAGE_TYPE_FROM_SERVER
jss = pack('<llhbb%ds'%(len(join)), len(join)+8, len(join)+8, msg_type, 0, 0, join)#发送入组消息
tcpClientSocket.send(jss)
m ={}
while True:
    m ={}
    data = tcpClientSocket.recv(4096)  # data就是接受到的消息
    if not data:
        time.sleep(0.01)
        continue
 #   print(data)
    buff = data.decode('latin-1')
#    print(buff)
    buff_len = len(buff)

    # print '[Packet] Packet buffer length %d' % buff_len

    if buff_len < 12:
        print(None)

    packet_length_1, packet_length_2, msg_type, encryption, reserved, body = unpack('<llhbb%ds' % (buff_len - 12),
                                                                                    bytes(buff, 'latin-1'))

    # print '[Packet] Packet length 1: %d' % packet_length_1
    # print '[Packet] Packet length 2: %d' % packet_length_2
    # print '[Packet] Packet msg_type: %s' % msg_type
    # print '[Packet] Packet encryption: %d' % encryption
    # print '[Packet] Packet reserved: %d' % reserved
    # print '[Packet] Packet body: %s' % body

   # if packet_length_1 != packet_length_2:
    #    print('[Packet] Unmatched packet length fields!')
     #   raise Exception()

    needed_body_length = packet_length_1 - 8
    current_body_length = len(body)

    if current_body_length < needed_body_length:
        # print '[Packet] Insufficient packet body data'
        print( None)

    if current_body_length > needed_body_length:
        body = body[0:needed_body_length]
        # print '[Packet] Packet body trimmed: %s' % body
    body = body.decode("utf-8")
    m_match = re.match(r'type@=chatmsg', body)#匹配 chatmsg
    if m_match:
        print(body)


    else:
        pass
    # print '[Packet] Packet detected: %s' % body


tcpClientSocket.close()

"""
服务器弹幕消息 b'\xea\x00\x00\x00\xea\x00\x00\x00\xb2\x02\x00\x00type@=chatmsg/rid@=122402/ct@=2/uid@=34626746/nn@=\xe7\xbb\x88\xe7\xa9\xb6\xe6\x98\xaf\xe6\xa2\xa6\xe4\xb8\x80/txt@=\xe6\x88\x91\xe4\xb8\x80\xe8\xbf\x9b\xe6\x9d\xa5\xe5\xb0\xb1\xe7\x9c\x8b\xe5\x88\xb0\xe5\xb8\xb8\xe5\xa8\x81\xe5\x86\x8d\xe6\x89\x93\xe6\x9d\xa5\xe7\xa6\x8f/cid@=f5ee35093ae4455f6e043c0000000000/ic@=avatar@Sdefault@S12/level@=2/sahf@=0/bnn@=/bl@=0/brid@=0/hc@=/el@=/lk@=/\x00\xf8\x00\x00\x00\xf8\x00\x00\x00\xb2\x02\x00\x00type@=chatmsg/rid@=122402/ct@=2/uid@=159122772/nn@=\xe5\x98\xbf\xe5\x93\x88666\xe4\xbd\xa0\xe6\xb2\xa1\xe7\x9a\x84/txt@=\xe6\x9d\xa5\xe7\xa6\x8f/cid@=f5ee35093ae4455f7c043c0000000000/ic@=avanew@Sface@S201803@S20@S08@S0b50716b79d016ae7d04249beeeb622f/level@=3/sahf@=0/bnn@=/bl@=0/brid@=0/hc@=/el@=/lk@=/\x00\x04\x01\x00\x00\x04\x01\x00\x00\xb2\x02\x00\x00type@=chatmsg/rid@=122402/uid@=5093704/nn@=\xe5\xa5\xbd\xe8\xbf\x90\xe6\xb0\x94\xe7\x8f\xad\xe5\xae\xbe\xe8\xaf\xba/txt@=\xe6\x88\x91\xe4\xb8\x80\xe8\xbf\x9b\xe6\x9d\xa5\xe5\xb0\xb1\xe7\x9c\x8b\xe5\x88\xb0\xe5\xb8\xb8\xe5\xa8\x81\xe5\x9c\xa8\xe6\x89\x93\xe6\x9d\xa5\xe7\xa6\x8f/cid@=f5ee35093ae4455f7e043c0000000000/ic@=avatar@S005@S09@S37@S04_avatar/level@=9/sahf@=0/cst@=1522908893083/bnn@=/bl@=0/brid@=0/hc@=/el@=/lk@=/\x00'

向斗鱼服务器发出的请求登陆信息格式为type@=loginreq/roomid@=85894/,通过二进制包要把信息发出
斗鱼协议如下表 所以要发送的数据流为mss = pack('<llhbb%ds'%(len(message_body)), len(message_body)+8, len(message_body)+8, msg_type, 0, 0, message_body)
这样mss即可通过socket.send()发送给服务端
要注意的是数据部分要在结尾加"\0",同时pack()中字符串要为二进制所以b"message_body值为type@=loginreq/roomid@=85894/\0"  其中b可将字符串转为二进制形式
pack()第一个参数表示的是 给定的格式(fmt) 具体见笔记(https://blog.csdn.net/w83761456/article/details/21171085)
字节  Byte 0  Byte 1  Byte 2  Byte 3 
长度             消息长度 
头部 
                消息长度 
     消息类型        加密字段  保留字段 
数据部  数据部分(结尾必须为‘\0’) 

"""