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
join = "type@=joingroup/rid@=122402/gid@=-9999/\0"
#msg_type = MESSAGE_TYPE_FROM_SERVER
jss = pack('<llhbb%ds'%(len(join)), len(join)+8, len(join)+8, msg_type, 0, 0, join.encode("utf-8","ignore"))#发送入组消息
tcpClientSocket.send(jss)
m ={}
while True:
    m ={}
    data = tcpClientSocket.recv(1024)  # data就是接受到的消息
    if not data:
        time.sleep(0.01)
        continue

    buff = data
    buff_len = len(buff)

    if buff_len < 12:
        print(None)
    try:
        packet_length_1, packet_length_2, msg_type, encryption, reserved, body = unpack('<llhbb%ds' % (buff_len - 12),
                                                                                    bytes(buff))

        needed_body_length = packet_length_1 - 8
        current_body_length = len(body)


        if current_body_length < needed_body_length:
            # print '[Packet] Insufficient packet body data'
            print( None)

        if current_body_length >= needed_body_length:
            body = body[0:needed_body_length]
            # print '[Packet] Packet body trimmed: %s' % body
            body = body.decode("utf-8")
            m_match = re.match(r'type@=chatmsg', body)#匹配 chatmsg
        else:
            m_match = None
        if m_match:
            print("m_match"+body)
        else:
            pass
    except BaseException as e:
        print(body)
        print(e)
        pass
    # print '[Packet] Packet detected: %s' % body


tcpClientSocket.close()
