# 目录树
import os
def travelTree(currentPath, count):
    if not os.path.exists(currentPath):
        print("no")
    if os.path.isfile(currentPath):
        #print("file")
        fileName = os.path.basename(currentPath)#os.path.basename(),返回path最后的文件名。若path以/或\结尾，那么就会返回空值。
        print("|"+'——' * count + '——' + fileName)#破折号
    elif os.path.isdir(currentPath):
        if count == 0:
            print( '——' * count + '|——' + currentPath)
        #print("dir")
        else:
            print("|"+'——' * count + '|——' + currentPath)
        pathList = os.listdir(currentPath)
        for eachPath in pathList:
            path = os.path.join(currentPath,eachPath)
            travelTree(path, count + 1)#递归

travelTree('E:\\', 0)#\要转义
