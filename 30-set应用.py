#set特点是元素没有重复的 所以可将list等转换为set去重
ls = [1,3,1,1,2,3,4,5,5,6,6]
s = list(set(ls))
print(s)