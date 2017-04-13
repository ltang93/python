# -*- coding: utf-8 -*-

L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[]
for x in L1 :
    if isinstance(x, str)==True:
        x=x.lower()
        L2.append(x)
print(L2)