import time
def test1():
    while True:
        print("............")
        yield None

def test2():
    while True:
        print("...............")
        yield None

t1 = test1()
t2 = test2()
while True :
    time.sleep(2)
    t1.__next__()
    time.sleep(2)
    t2.__next__()


"""多任务执行----协程"""