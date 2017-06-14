import random
a=[random.randint(0,100) for i in range(100)]
b=[]
for i in range(len(a)):
    b.append(a[i])
print(a==b)