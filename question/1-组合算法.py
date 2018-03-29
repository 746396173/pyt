"""
itertools.combinations(iterable, r)
iterable是迭代器(对象)每一个元素都是独立成分
r是迭代长度，默认为可获得的最大长度迭代

作用:返回连续长度为r的的迭代器(对象)所有可能组合"""
"""需求是从数组 N 中获取长度为 M 的集合 example N = [1,2,3,4,5] M=3, 那么输出为 [{1,2,3}{1,2,4},{1,2,5},{2,3,4},{2,3,5}{3,4,5}]"""

import itertools
def zuhe (iterable,r):
	for item in itertools.combinations(iterable,r):
		print(item)

#combinations 实现方法
def combinations(iterable, r): #
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)#列表转变为元组
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))#[0,1,2]
    yield tuple(pool[i] for i in indices)#调用函数执行到这时会返回一个元组并记住位置等待下次调用时继续向下执行

    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r: #2:6 1;5 0;4
                break#结束循环
        else:
            return#结束
        indices[i] += 1#indices[2]=3 indices[1] = 2
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)



if __name__ =="__main__":
#    zuhe("woyebuzhidao",3)
#    zuhe([1,2,3,4,5,6,7],3)
    lis = range(1,32)
    zuhe(lis ,6)