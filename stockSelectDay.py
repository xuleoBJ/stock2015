# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Cstock
import Ccomfunc
import pdb
import stockTrendAna
import numpy as np
import getStockIDList


## 根据历史日涨幅选股，输入strMonth = "01" strDay ="31"
def selectStockByDayRise(strMonth,strDay,stockIDList):
    lineWritedList=[]
    lineWritedList8=[]
	
    print (u"条件筛选股票："+strMonth+strDay)
    ##分析板块指数月度数据的涨幅，进行股票板块筛选，这是周期性行情选择的一个主要方法
    headLine=[]
    headLine.append("stockID")
    headLine.append("stockName")
    headLine.append("date")
    headLine.append("rise(%)")
    headLine.append("date")
    headLine.append("rise(%)")
    headLine.append("date")
    headLine.append("rise(%)")
    headLine.append("date")
    headLine.append("rise(%)")
    headLine.append("date")
    headLine.append("rise(%)")
    headLine.append("date")
    headLine.append("rise(%)")
	
    dayStrList=[ ele+"/"+strMonth+"/"+strDay for ele in ["2011","2012","2013","2014","2015"]]
    for stockID in stockIDList:
        ##读取股票代码，存储在curStock里
        curStock=Cstock.Stock(stockID)
        if curStock.count > 0 : 
            sList=[]
            sList.append(curStock.stockID)
            sList.append(curStock.stockName)
            for sDay in dayStrList:
                indexOfDate=Ccomfunc.getIndexByStrDate(curStock,sDay)
                sList.append( curStock.dayStrList[indexOfDate]+"["+str(curStock.weekDayList[indexOfDate])+"]" )
                riseRate = -999
                if indexOfDate>=0:
                    riseRate = curStock.dayRiseRateCloseArray[indexOfDate] 
                sList.append(str(riseRate))
            if stockID[0] not in ["3","6","0"]:
                lineWritedList8.append("\t".join(sList))
            else:
                lineWritedList.append("\t".join(sList))
    goalFilePath=os.path.join( Ccomfunc.resultDir,strMonth+strDay+u'_stockRise股票.txt')
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    goalFilePath=os.path.join( Ccomfunc.resultDir,strMonth+strDay+u'_stockRise板块.txt')
    Ccomfunc.write2Text(goalFilePath,lineWritedList8)


def logRecord(logFilePath,startClock,strDay):
    logFileWrited=open(logFilePath ,'a')
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
    logFileWrited.write(strDay+"\t"+str(round(timeSpan,2))+"\n")
    logFileWrited.close()

if __name__=="__main__":
    
    curFilename=os.path.basename(__file__)
    logFilePath=os.path.join(u'log_'+curFilename+'.txt')

    stockIDList = getStockIDList.makeStockList()
    strMonth="07"
    dayRange=range(20,31)
    for i in dayRange:
        startClock=time.clock() ##记录程序开始计算时间
        strDay = str(i).zfill(2)
        selectStockByDayRise("07",strDay,stockIDList)
        logRecord(logFilePath,startClock,strMonth+strDay)


