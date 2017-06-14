import random
x=random.randint(0,1000)
y=''
print(x)
while(x>0):
    y=str(x%2)+y
    x=x//2
print(y)