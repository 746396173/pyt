
'''执行时调试
程序启动，停止在第一行等待单步调试。

python -m pdb some.py
交互调试
进入python或ipython解释器

import pdb
pdb.run('testfun(args)') #此时会打开pdb调试，注意：先使用s跳转到这个testfun函数中，然后就可以使用l看到代码了
程序里埋点
当程序执行到pdb.set_trace() 位置时停下来调试

代码上下文
...

import pdb
pdb.set_trace()

...'''