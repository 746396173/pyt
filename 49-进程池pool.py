from multiprocessing import Pool
import os ,time ,random
def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d"%(msg,os.getpid()))
    time.sleep(random.random()*2)
    #random.random()随机生成0-1之间的浮点数
    t_stop = time.time()
    print(msg,"执行完毕,耗时%0.2f"%(t_stop - t_start))

if __name__ =="__main__":
    po = Pool(3)#定义一个进程池,最大同时进程数3
    for i in range(0,10):
    #Pool.apply_async(要调用的目标,(传递给目标的参数元祖,))
    #每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker,(i,))#非阻塞式执行

    print("----start----")
    po.close()#关闭进程池,关闭后po不再接收新的请求
    po.join()#必须放在close()之后执行
    print("------end-------")


"""
multiprocessing.Pool常用函数解析：

apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程），args为传递给func的参数列表，kwds为传递给func的关键字参数列表；

apply(func[, args[, kwds]])：使用阻塞方式调用func

close()：关闭Pool，使其不再接受新的任务；

terminate()：不管任务是否完成，立即终止；

join()：主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；
"""