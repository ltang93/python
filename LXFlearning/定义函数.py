# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    return(((-b+math.sqrt(b**2-4*a*c))/(2*a)),((-b-math.sqrt(b**2-4*a*c))/(2*a)))

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))