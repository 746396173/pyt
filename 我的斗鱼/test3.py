import re
import time
import socket
import multiprocessing
from struct import pack, unpack
import pymysql
#打开数据库连接
db = pymysql.connect("localhost","root","121115","test1",charset='utf8')
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

def shujuku(ui,u,d):
    global cursor,db
    uid =ui
    user =u
    danmu =d

    # SQL 插入语句
    sql = """INSERT INTO dm(uid,user,danmu)
         VALUES ('%s','%s','%s')"""%(uid,user,danmu)#注意写法
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行插入
       db.commit()
    except BaseException as e:
        print(danmu)
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
    pattern1 = r"nn@=[\S]+/txt@="   #昵称     \s	匹配任意空白字符，等价于 [\t\n\r\f]。\S 匹配任意非空字符，有空格则不符合
    pattern2 = r"/txt@=[\S\s]+/cid@="#弹幕     匹配任意字符
    pattern3 = r"/uid@=[\S]+/nn@="#用户uid

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
        m_match = False
        m = {}
        data = tcpClientSocket.recv(1024)  # data就是接受到的消息
        if not data:
            # time.sleep(0.01)
            continue

        buff = data
        buff_len = len(buff)

        if buff_len < 12:
            print(None)
        try:
            packet_length_1, packet_length_2, msg_type, encryption, reserved, body = unpack(
                '<llhbb%ds' % (buff_len - 12),
                bytes(buff))

            needed_body_length = packet_length_1 - 8
            current_body_length = len(body)

            if current_body_length < needed_body_length:
                # print '[Packet] Insufficient packet body data'
                #print(None)
                pass

            if current_body_length >= needed_body_length:
                body = body[0:needed_body_length]
                # print '[Packet] Packet body trimmed: %s' % body
                body = body.decode("utf-8")
                m_match = re.match(r'type@=chatmsg', body)  # 匹配 chatmsg
            else:
                m_match = False
            if m_match:
                ret1 = re.search(pattern3, body).group()[6:-5]
                ret2 = re.search(pattern1, body).group()[4:-6]
                ret3 = re.search(pattern2, body).group()[6:-6]
                #写入数据库
                shujuku(ret1,ret2,ret3)
                #控制台输出
                #print(str(dm_n) + "-->" +ret1 + ret2 + ":" + ret3)
                dm_n += 1

            else:
                pass
        except BaseException as e:
            print(body)
            print(e)
            pass

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
