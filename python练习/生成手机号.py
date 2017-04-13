head=input('输入手机号开头3位：')
count=input('输入要生成的个数：')
fg=input('输入分隔符：')
numfile=open('D://number.txt','w')

for i in range(int(count)):
    numfile.write('%s%s'%(int(head)*100000000+i,fg))
    numfile.write('\n',)
numfile.close()
print('ok')