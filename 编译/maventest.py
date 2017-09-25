import os,shutil

start='1767'
end='HEAD'
svnurl='http://10.2.2.152/svnswt/swt_cms/CODE'
inurl=r'D://jenkins/workspace/swt_cms/target/swt_cms-1.0.0'
outurl=r'C://Users/wangmeng_c/Desktop/swt_cms/target/swt_cms-1.0.0'
# cmd='svn diff -r   1767:HEAD --summarize http://10.2.2.152/svnswt/swt_cms/CODE'
if not os.path.isdir(outurl):
    os.makedirs(outurl)
cmd='svn diff -r '+start+':'+end+' --summarize '+svnurl
result=os.popen(cmd)
for line in result:
    if line[0]!='D':
        print(line,end='')
        if line[0] != 'D':
            lineurl=line[1:].replace(svnurl,'')
            print(lineurl,end='')
            saveurl=lineurl.replace('/src/main/activeResources/dev','/WEB-INF/classes').replace('/src/main/java','/WEB-INF/classes').replace('/src/main/resources','/WEB-INF/classes').replace('/src/main/webapp','/').replace('//','/').replace('java','class').strip()
            if '/src/main/resources/mybatisGeneratorCfg' not in saveurl:
                print(inurl+saveurl) #取文件
                print(outurl+saveurl) #存储
                # print('/'.join(saveurl.split('/')[1:-1]))
                # print(outurl+'/'+'/'.join(saveurl.split('/')[1:-1]))
                if 'WEB-INF/classes/mybatisGeneratorCfg' in inurl+saveurl:
                    continue
                if not os.path.isdir(outurl+'/'+'/'.join(saveurl.split('/')[1:-1])):
                    os.makedirs(outurl+'/'+'/'.join(saveurl.split('/')[1:-1]))
                shutil.copy(inurl+saveurl,outurl+saveurl)