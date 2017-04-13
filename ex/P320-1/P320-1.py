import random
xrc=open('xrc.txt','r')
mc=open('mc.txt','r')
dcdy=open('dcdy.txt','r')
fcdy=open('fcdy.txt','r')

xrclist=xrc.readline()
mclist=mc.readline()
dcdylist=dcdy.readline()
fcdylist=fcdy.readline()

xrc.close()
mc.close()
dcdy.close()
fcdy.close()

xrcflist=xrclist.split(',')
mcflist=mclist.split(',')
dcdyflist=dcdylist.split(',')
fcdyflist=fcdylist.split(',')

print("The",random.choice(xrcflist),random.choice(mcflist),random.choice(dcdyflist),random.choice(fcdyflist))
