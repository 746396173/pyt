from socket import *
import multiprocessing
import threading

dup_socket = socket(AF_INET,SOCK_DGRAM)
bindAddr = ('', 8888) # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
dup_socket.bind(bindAddr)
def send_():

    while True:
        send_Data = input("")
        Adder_ = ("192.168.0.102", 8080)
        dup_socket.sendto((send_Data).encode("gb2312"), Adder_)

def shou_():

    while True:
        recvData = dup_socket.recvfrom(1024)
        a, b = recvData
        # a = recvData[0]
        print(a.decode("gb2312"))

if __name__ == "__main__":
    p1 = threading.Thread(target=send_)
    p2 = threading.Thread(target=shou_)

    p1.start()
    p2.start()
