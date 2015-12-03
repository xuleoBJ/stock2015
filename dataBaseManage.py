import os
import sqlite3

def createDataBase(dataBasePath):
    if not os.path.exists(dataBasePath):
        conn = sqlite3.connect(dataBasePath)
        cur = conn.cursor()
        
        sqlCreateTable_tradetactics='''create table IF NOT EXISTS tradeTactics (date text PRIMARY KEY, tradetactics text , comment text )'''
        cur.execute(sqlCreateTable_tradetactics)
       
        cur.close()
        conn.close()
        print("Database is created.")
    else:
        print("Database is exist.")

def insertData2TradeTactics(_cur,sDate,tradetactics,comment):
    sql_insert = u"REPLACE INTO tradetactics(date,tradetactics,comment) values (?,?,?)"
    print sql_insert
    try:
        _cur = conn.cursor()
        _cur.execute(sql_insert,(sDate,tradetactics,comment))
        print(sDate+' update data completed.')
    except sqlite3.Error, e:
        print 'insert record failed.',e

def selectData2TradeTactics(_cur,sDate):
    sql_select = u"SELECT * FROM tradetactics WHERE date = {}".format(sDate)
    print sql_select
    try:
        _cur = conn.cursor()
        _cur.execute(sql_select)
        print _cur.fetchone()
    except sqlite3.Error, e:
        print 'no record ',e

if __name__=="__main__":
    dbasePath="dataManage\\stock_xl.db"
    createDataBase(dbasePath)
    lineIndex=0
    conn = sqlite3.connect(dbasePath)
    cur = conn.cursor()
    insertData2TradeTactics(cur,"20080808","hello","hello")
    selectData2TradeTactics(cur,"20080808")
    cur.close()
    conn.commit()
    conn.close()


    
    
