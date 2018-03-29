# -*- coding:utf-8 -*-
L1 = ['Hello','World',18,'Apple',None]
L2 = [word for word in L1 if isinstance(word,str)]
print(L2)