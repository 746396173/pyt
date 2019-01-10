import re
import time
import socket
import multiprocessing
from struct import pack, unpack
import pymysql
#打开数据库连接
db = pymysql.connect("localhost","root","123456","test1",charset='utf8')
#使用cursor（）方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute（）方法执行 SQL查询
cursor.execute("SELECT VERSION()")

# 使用fetchone（）方法获取单条数据
data = cursor.fetchone()
#print("databse version:%s" % data)

MESSAGE_TYPE_FROM_CLIENT = 689
MESSAGE_TYPE_FROM_SERVER = 690
tcpClientSocket = None

def shujuku(u,d):
    global cursor,db
    user =u
    danmu =d

    # SQL 插入语句
    sql = """INSERT INTO dm2(user,danmu)
         VALUES ('%s','%s')"""%(user,danmu)#注意写法
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行插入
       db.commit()
    except BaseException as e:
        print(e)
        db.rollback()
       # 如果发生错误则回滚
def lian():
    serAddr = ('openbarrage.douyutv.com', 8601)
    tcpClientSocket = socket.create_connection(serAddr)
    print("socket信息" + str(tcpClientSocket))
    return tcpClientSocket

def d_m(t, room):
    room = room
    pattern1 = r"nn@=[\S]+/txt@="
    pattern2 = r"/txt@=[\S]+/cid@="

    tcpClientSocket = t
    dm_n = 0
    message_body = b'type@=loginreq/roomid@=%d/\0' % (room)  # 转义后要发送的 数据部分字符串必须是二进制的
    msg_type = MESSAGE_TYPE_FROM_CLIENT
    mss = pack('<llhbb%ds' % (len(message_body)), len(message_body) + 8, len(message_body) + 8, msg_type, 0, 0,
               message_body)  # 打包成二进制流
    tcpClientSocket.send(mss)  # 发送
    #	接收对⽅发送过来的数据，最⼤接收1024个字节
    recvData = tcpClientSocket.recv(4096)  # 收到的是二进制流
    print("服务器返回值1" + str(recvData))
    join = "type@=joingroup/rid@=%d/gid@=-9999/\0" % (room)
    jss = pack('<llhbb%ds' % (len(join)), len(join) + 8, len(join) + 8, msg_type, 0, 0, join.encode("utf-8"))  # 发送入组消息
    tcpClientSocket.send(jss)
    m = {}
    while True:
        m = {}
        data = tcpClientSocket.recv(1024)  # data就是接受到的消息
        if not data:
            # time.sleep(0.01)
            continue
        try:
            buff = data.decode('latin-1')
            buff_len = len(buff)
            # print(str(data))
            if buff_len < 12:
                # print(None)
                pass
            packet_length_1, packet_length_2, msg_type, encryption, reserved, body = unpack(
                '<llhbb%ds' % (buff_len - 12),
                bytes(buff, 'latin-1'))
        except:
            continue

        needed_body_length = packet_length_1 - 8
        current_body_length = len(body)

        if current_body_length < needed_body_length:
            pass

        if current_body_length > needed_body_length:
            body = body[0:needed_body_length]
        try:

            body = body.decode("utf-8")
            m_match = re.match(r'type@=chatmsg', body)  # 匹配 chatmsg
            if m_match:
                ret1 = re.search(pattern1, body).group()[4:-6]
                ret2 = re.search(pattern2, body).group()[6:-6]
                #写入数据库
                shujuku(ret1,ret2)
                #控制台输出
                #print(str(dm_n) + "-->" + ret1 + ":" + ret2)
                dm_n += 1

            else:
                pass
        except:
            pass
    tcpClientSocket.close()
    db.close()

def keeplive(t):
    tcpClientSocket = t
    # 保持心跳，15秒心跳请求一次
    while True:
        message_body = b'type@=mrkl/" + \0'
        msg_type = MESSAGE_TYPE_FROM_CLIENT
        mss = pack('<llhbb%ds' % (len(message_body)), len(message_body) + 8, len(message_body) + 8,
                   msg_type, 0, 0,message_body)  # 打包成二进制流
        tcpClientSocket.send(mss)  # 发送
        print('发送心跳包')
        time.sleep(44)

if __name__ == "__main__":
    t = lian()
    room = input("输入房间号：")  # 78622
    room = int(room)
    # print(t)
    p1 = multiprocessing.Process(target=d_m, args=(t, room))
    p2 = multiprocessing.Process(target=keeplive, args=(t,))
    print("-------start---------")
    p1.start()
    p2.start()

    print("--------end------------")
