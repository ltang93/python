# -*- coding: utf-8 -*-
from functools import reduce

def mi(x,y):
    return x*y

def prod(L):
    return reduce(mi,L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))