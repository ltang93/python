# -*- coding: utf-8 -*-

from functools import reduce

def add(x,y):
    print('add')
    return x+y

def spl(z):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[z]
    x,y=s.split('.')
    x=int(x)
    y=float('0.'+y)
    return x,y

def str2float(s):
    return reduce(add,map(spl,s))


print('str2float(\'123.456\') =', str2float('123.456'))

#不会