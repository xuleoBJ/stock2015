# -*- coding: cp936 -*-
import os
import sqlite3

def readFaultPointFileIntoDataBase(dataBasePath,faultfilePath,_tableName):
    ##Logfile 第一行为 测井名，列数相同！
    _conn = sqlite3.connect(dbasePath)
    _cur = _conn.cursor()
    lineIndex=0
    for line in open((logfilePath),'r'):
        splitLine=line.split()
        lineIndex=lineIndex+1
        if  lineIndex==1 :
            sqlDropTable_log_table="DROP TABLE IF EXISTS %s"%(log_tableName)
            _cur.execute(sqlDropTable_log_table)
            _tableField=' real, '.join(splitLine)+' real'
            sqlCreateTable_log_table="create table IF NOT EXISTS %s (%s)"%(log_tableName,_tableField)
##            print sqlCreateTable_log_table
            _cur.execute(sqlCreateTable_log_table)
        if  lineIndex>1 and len(splitLine)>1:
            insertedItem=','.join(splitLine)
            sql_desc = "REPLACE INTO %s values(%s)"%(log_tableName,insertedItem)
##            print(sql_desc)
            try:
                _cur.execute(sql_desc)
            except sqlite3.Error, e:
                print ('insert record failed.',e)
    _cur.close()
    _conn.commit()
    _conn.close()
    print('import %s completed.'%(logfilePath))







if __name__=="__main__":
    dbasePath="xulei_test.db"
    sourceDirPath="_data\_log"
    fileNames=os.listdir(sourceDirPath)
    for fileItem in fileNames:
        log_tableName='\"log_'+fileItem.replace('.txt','\"')
        logfilePath=os.path.join(sourceDirPath,fileItem)
        readLogfileIntoDataBase(dbasePath,logfilePath,log_tableName)
##        fileOpened=open(sourceDirPath+'\\'+fileItem,'r')
##        for line in fileOpened.readlines():
##            fileWrited.write(line)
##    importLog(dbasePath)
##    lineIndex=0
##    conn = sqlite3.connect(dbasePath)
##    log_tableName='log_sha40'
##    cur = conn.cursor()
##    for line in open(("_data\_log\sha40.txt"),'r'):
##        splitLine=line.split()
##        lineIndex=lineIndex+1
##        if  lineIndex==1 :
##            _tableField=' real, '.join(splitLine)+' real'
####            for item in splitLine:
####                _tableField=_tableField+item+" real, "
####                _tableField.rstrip()
##            sqlDropTable_log_table="DROP TABLE IF EXISTS %s"%(log_tableName)
##            cur.execute(sqlDropTable_log_table)
##            sqlCreateTable_log_table="create table IF NOT EXISTS %s (%s)"%(log_tableName,_tableField)
##            
##            print sqlCreateTable_log_table
##            cur.execute(sqlCreateTable_log_table)
##        if  lineIndex>1 and len(splitLine)>1:
##            insertedItem=','.join(splitLine)
##            
##            sql_desc = "REPLACE INTO %s values(%s)"%(log_tableName,insertedItem)
####            print sql_desc
##            try:
##                cur.execute(sql_desc)
##            except sqlite3.Error, e:
##                print 'insert record failed.',e
            


    


    
    
