import multiprocessing
import time

def test(msg):
    while True:
        print("%s---test---"%(msg))
        time.sleep(1)


def test2():
    while True:
        print(".....test2......")
        time.sleep(3)


if __name__=="__main__":#这句话要写上在win下使用多进程时，要有入口（if __name__=='__main__':），Pool要包装在函数内，再调用。
    p = multiprocessing.Process(target=test,args=('参数',))
    t = multiprocessing.Process(target = test2)

    p.start() #让这个进程开始执行test函数里的代码
    t.start()
    while True:
        print("---main---")
        time.sleep(3)

