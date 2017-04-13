# -*- coding: utf-8 -*-

def is_palindrome(n):
    long=len(str(n))
    if long==1:
        return False
    i,x,y=0,0,-1
    while i<long:
        if str(n)[x]==str(n)[y]:
            i=i+1
            x=x+1
            y=y-1
        else:
            return False
    return True

# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))