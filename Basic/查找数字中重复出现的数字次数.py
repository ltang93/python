from collections import Counter
a=9820394857487123490878957943
b=str(a)[0:10]
c=Counter(b)
print(c)

a=9820394857487123490878957943
b=str(a)[0:10]
c={}
for i in b:
    if c.get(i,-1)==-1:
        c[i]=1
    else:
        c[i]=c[i]+1
print(c)