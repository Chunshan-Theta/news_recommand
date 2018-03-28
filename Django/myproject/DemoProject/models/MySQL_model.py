#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
#reload(sys)                         # 2
#sys.setdefaultencoding('utf-8')     # 3





# 引入 MySQLdb 模組，提供連接 MySQL 的功能
import pymysql as MySQLdb

# 連接 MySQL 資料庫
#db = MySQLdb.connect(host="xxx.xxxx.xxxx.xxxx",user="root", passwd="root_password", db="db_liat_name",charset='utf8')

try:
    pass#print "-- DB commend: test connent to DB "
    db = MySQLdb.connect(host="localhost",user="root", passwd="root", db="test",charset='utf8')
    cursor = db.cursor()
    pass#print "-- DB commend: close test connection to DB"
    db.close()
except Exception as e:
    pass#print "\n\n\n***** SQL connect ERROR : "+str(e)+'*****\n\n\n'


def status():
    if db.open:
        pass#print '-- DB status: connection is open'
    else:
        pass#print '-- DB status: connection is closed'

def connectDB(Thost="localhost",Tuser="root", Tpasswd="root", Tdb="news",Tcharset='utf8'):
    pass#print "-- DB commend: connent to DB "+str(Thost)
    global db,cursor
    db = MySQLdb.connect(host=Thost,user=Tuser, passwd=Tpasswd, db=Tdb,charset=Tcharset)
    cursor = db.cursor()

def close():
    pass#print "-- DB commend: close connection to DB"
    db.close()

def exeSQl(sql):
    pass#print '-- SQL commend: '+str(sql)
    # 執行 MySQL 查詢指令
    cursor.execute(sql)
    db.commit()
    # 取回所有查詢結果
    results = cursor.fetchall()
    '''
    # 輸出結果
    for record in results:
        row = ""
        for col in record:
            row += str(col).replace("\n", "")
            row += ","        
        pass#print row
    '''
    return results
