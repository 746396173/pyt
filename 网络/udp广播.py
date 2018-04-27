import socket, sys

dest = ("<broadcast>",8080)
adder1 = ('',8090)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

s.bind(adder1)

s.sendto("hi".encode("gb2312"),dest)
print("dengdaihuifu")

while True:
        buf,adderss = s.recvfrom(2048)
        print("receivedfrom %s:%s"%(adderss, buf))

s.close()
