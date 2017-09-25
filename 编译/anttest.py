import os,shutil


def saveurl(lineurl):
    saveurl = lineurl.replace('/lib', '/webapp/WEB-INF/lib').replace('/src/applicationContext_autoSaveSampleMMS.xml',
                                                                     '/bin/applicationContext_autoSaveSampleMMS.xml').replace(
        '/src/sql-map-config.xml', '/bin/sql-map-config.xml').replace(
        '/src/com/aspire/boc/mms/util/AutoSaveSampleMMS.java',
        '/bin/com/aspire/boc/mms/util/AutoSaveSampleMMS.java').replace(
        '/src/com/aspire/boc/mms/util/AutoCleanMMContent.java',
        '/bin/com/aspire/boc/mms/util/AutoCleanMMContent.java').replace('//', '/').replace('java', 'class').strip()
    # if '/src/main/resources/mybatisGeneratorCfg' not in saveurl:
    print('in  '+inurl + saveurl)  # 取文件
    print('out  '+outurl + saveurl)  # 存储
    # print('/'.join(saveurl.split('/')[1:-1]))
    # print(outurl+'/'+'/'.join(saveurl.split('/')[1:-1]))
    if 'WEB-INF/classes/com/aspire/boc/mms/test' in inurl+saveurl:
        return
    try:
        file=outurl + '/' + '/'.join(saveurl.split('/')[1:-1])
        if not os.path.isdir(file):
            os.makedirs(file)
            print('make '+file)
        shutil.copy(inurl + saveurl, outurl + saveurl)
        print('copy '+inurl + saveurl+' to '+outurl + saveurl)
    except PermissionError:
        shutil.rmtree(outurl + '/' + '/'.join(saveurl.split('/')[1:]))
        print(outurl+' '+''.join(saveurl.split('/')[1:]))
        print('rm '+outurl + '/' + '/'.join(saveurl.split('/')[1:]))
        shutil.copytree(inurl + saveurl, outurl + saveurl)
    except:
        print('error')

start='673'
end='HEAD'
svnurl='http://10.2.2.152/svnmms/cms/cms_platform/CODE'
inurl=r'D://jenkins/workspace/cms_platform/release/aspire-mms-cms'
outurl=r'C://Users/wangmeng_c/Desktop/cms_platform/release/aspire-mms-cms'
# cmd='svn diff -r   673:HEAD --summarize http://10.2.2.152/svnswt/swt_cms/CODE'
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
            if '/src/com/' in lineurl:
                lineurl=lineurl.replace('/src/com/','/webapp/WEB-INF/classes/com/')
                print('saveurl src com ' + lineurl)
                saveurl(lineurl)
                continue
            if '/src/' in lineurl:
                # if '.xml' or '.properties' or '.txt' or '.vm' in lineurl:
                if 'applicationContext' in lineurl or 'sql-map-config.xml' in lineurl or 'jdbc.properties' in lineurl:
                    lineurl1=lineurl
                    lineurl1=lineurl1.replace('/src/','/webapp/WEB-INF/')
                    print('saveurl src1 '+lineurl1)
                    saveurl(lineurl1)

                lineurl=lineurl.replace('/src/','/webapp/WEB-INF/classes/')
                print('saveurl src2 ' + lineurl)
                saveurl(lineurl)
                continue
            else:
                saveurl(lineurl)
shutil.copytree(inurl+'/bin', outurl + '/bin')

