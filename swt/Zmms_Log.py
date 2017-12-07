import time,pymysql,random,uuid

def DbConnect(sql):
    db = pymysql.connect(host='192.168.136.26', port=3306, user='ZMMS', password='ZMMS', db='mmststdb', charset='utf8')
    cursor = db.cursor()
    cursor.execute(sql)
    # 使用 fetchone() 方法获取单条数据.
    db.commit()
    db.close()

def MtLog(ec,gw,mms,task,product,free,mobile):
    # print(ec,gw,mms,task,product,free,biz)
    #INSERT INTO `MTLOG` VALUES (null, '60', '1', '112', '117', '69', '13810021371', '1135', 'm1', null, '1', null, '1001', null);
    # sql='''INSERT INTO `MTLOG` VALUES (null, '60', '1', '112', '117', '69', '13810021371', '1135', 'm1', null, '1', null, '1001', null);'''
    count=random.randint(1,5000)
    print(count)
    j=0
    k=0
    l=0
    for i in range(count):
        status=random.randint(0,1)
        mobile=int(mobile)+1
        biz=uuid.uuid1()
        # print(biz)
        if status == 0:
            j=j+1
        sql = "INSERT INTO `MTLOG` VALUES(null,'%s','%s','%s','%s','%s','%s','1','%s','%s','%s',null,'%s',null)" % (ec,gw,mms,task,product,'1'+str(mobile),str(biz),time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ,free,status)
        # print(sql)
        DbConnect(sql)
        if status ==0:
            d=DLog(gw,biz)
            if d==0:
                k=k+1
            r=RLog(gw,biz)
            if r==0:
                l=l+1
    print('taskid: '+str(task),'MTsuccess: '+str(j),'Dsuccess: '+str(k),'Rsuccess: '+str(l))

def DLog(gw,biz):
    #INSERT INTO `DLOG` VALUES ('6', '1', '1', 'm2', '404', '13810021371', '2017-11-27 15:26:46', null);
    tf=random.randint(0,1)
    status=1
    if(tf==1):
        status = random.randint(0, 1)
        sql = "INSERT INTO `DLOG` VALUES (null, '1', '%s', '%s', '%s', null, '%s', null)" % (gw,biz,status,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
        # print(sql)
        DbConnect(sql)
    return status

def RLog(gw,biz):
    tf=random.randint(0,1)
    status=1
    if(tf==1):
        status = random.randint(0, 1)
        sql = "INSERT INTO `RLOG` VALUES (null, '%s', '%s', '%s',null, '%s', null)" % (gw,biz,status,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
        # print(sql)
        DbConnect(sql)
    return status

if __name__ == '__main__':
    tasks={'ec':('63','63','63','63','63','63'),'gw':('1','1','1','1','1','1'),'mms':('252','253','254','255','256','257'),'task':('263','264','265','266','267','268'),'product':('77','77','77','83','83','83'),'free':('0','0','0','1','1','1')}
    MoStart=str(time.strftime('%Y%m%d',time.localtime(time.time()))+'0000')[2:]
    # print(str(tasks['ec'][0]))
    i=0
    for ec in tasks['ec']:
        MtLog(tasks['ec'][i],tasks['gw'][i],tasks['mms'][i],tasks['task'][i],tasks['product'][i],tasks['free'][i],MoStart)
        i=i+1
