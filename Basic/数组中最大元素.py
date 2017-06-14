import random
a=[random.randint(0,100) for i in range(100)]
max=a[0]
for i in a:
    if i>max : max=i
print(max)
