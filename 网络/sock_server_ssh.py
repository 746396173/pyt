import socket ,os
server = socket.socket()
server.bind(("localhost",9999))
server.listen()
while True:
    conn,addr = server.accept()
    print("new conn:",addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令:",data.decode("utf-8"))
        cmd_res = os.popen(data.decode()).read()#os.popen() 方法用于从一个命令打开一个管道。
        conn.send(cmd_res.encode("utf-8"))

server.close()