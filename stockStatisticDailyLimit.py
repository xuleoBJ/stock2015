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
def selectStockByDailyLimit(strMonth,strDay,stockIDList):
    lineWritedList=[]
    lineWritedList8=[]
	
    print (u"统计涨停股票："+strMonth+strDay)
    ##分析板块指数月度数据的涨幅，进行股票板块筛选，这是周期性行情选择的一个主要方法
    headLine=[]
    headLine.append("stockID")
    headLine.append("stockName")
    headLine.append("当日涨幅(%)")
    headLine.append("次日涨幅(%)")
	
    dayStrList=[ ele+"/"+strMonth+"/"+strDay for ele in ["2011","2012","2013","2014","2015","2016"]]
    for stockID in stockIDList:
        ##读取股票代码，存储在curStock里
        curStock=Cstock.Stock(stockID)
        if curStock.count > 0 : 
            sList=[]
            for sDay in dayStrList:
                indexOfDate= curStock.dayStrList.index(sDay)
                if indexOfDate >= 0 :
                    sList.append(curStock.stockID)
                    sList.append(curStock.stockName)
                    sList.append( curStock.dayStrList[indexOfDate])
                    sList.append( curStock.dayRiseRateCloseFList[indexOfDate])
                    sList.append( curStock.dayRiseRateCloseFList[indexOfDate+1])
                    break 
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

    stockIDList = getStockIDList.makeStockList(1)

    ##构建按年月日数据表 年月日 股票代码 涨幅
    strMonth="08"
    dayRange=range(20,31)
    for i in dayRange:
        startClock=time.clock() ##记录程序开始计算时间
        strDay = str(i).zfill(2)
        selectStockByStrDateRise(strMonth,strDay,stockIDList)
        logRecord(logFilePath,startClock,strMonth+strDay)



