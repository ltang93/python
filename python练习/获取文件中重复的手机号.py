import re

a=[]
tfile=open('E://2017//巴基斯坦压测//巴基斯坦-短信-0313//20170313-1-2.log','r')
for i in range(201000):
    neirong=tfile.readline()
    phoneNumRegex=re.compile(r'Dest_terminal_Id=([0-9]{12})')
    mo=phoneNumRegex.search(neirong)   #若无，则返回None
    if mo !=None:
        if mo.group() in a:
            #print(mo.group())
            outfile = open('D://1.txt', 'a')
            outfile.write(mo.group()+'\n')
        else:
            a.append(mo.group())
tfile.close()
outfile.close()
print('ok')


'''
#Python正则表达式：
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # r''=原始字符
mo=phoneNumRegex.search('Nuber is 111-222-3333.')
print('Phone number is:' + mo.group() )

1.只有一行  open('D://1.txt', 'w'）
2.没有换行 outfile.write(mo.group())
3.每行之间有空行 outfile.write(mo.group()+'\r\n')
4.不写文件 print(mo.group())
'''