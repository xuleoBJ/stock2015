import os
import sqlite3

def createDataBase(dataBasePath):
    if not os.path.exists(dataBasePath):
        conn = sqlite3.connect(dataBasePath)
        cur = conn.cursor()
        
        sqlCreateTable_tradeInfor='''create table IF NOT EXISTS tradeInfor (date date PRIMARY KEY, infor text , comment text )'''
        cur.execute(sqlCreateTable_tradeInfor)
       
        cur.close()
        conn.close()
        print("Database is created.")
    else:
        print("Database is exist.")



if __name__=="__main__":
    dbasePath="stock_xl.db"
    createDataBase(dbasePath)
    lineIndex=0
    conn = sqlite3.connect(dbasePath)
    cur = conn.cursor()
    cur.close()
    conn.commit()
    conn.close()
    print('import data completed.')


    
    
