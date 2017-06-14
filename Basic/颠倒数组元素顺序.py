import random
a=[random.randint(0,100) for i in range(20)]
print(a)
l=len(a)
for i in range(int(l/2)):
    a[i]=a[l-1-i]
print(a)