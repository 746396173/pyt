__all__ = ["text1","text2"]#用from 包名 import * 时导入的模块
#import text1 #python2 导入包时直接导入的模块
print("执行了init.py")
from . import text1 	# python3 直接导入包时导入的模块
