with open("test.txt", "r+") as nf:  # 打开一个文件 如不存在则创建
    nf.write("a")
    nfr = nf.readline()
print(nfr)
