import random
a=[random.randint(0,100) for i in range(100)]
sum=0
for i in a:
    sum+=i
print(sum/len(a))