# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Cstock
import Ccomfunc
import pdb
import trendAna
import numpy as np


##两种方法获得stockIDList，selectScale=1 从文本文件stockIDList.txt 读取 =2，海选
def makeStockList(selectScale=2):
    stockIDList=["999999","399001"]
    ## 根据文件名的第一个字符区分股票类别  上证6 深圳 0 板块指8 创业板 3
    stockIDType=["8","3","6","0"]
    if selectScale == 1: ##限选
        with open('stockIDList.txt') as fOpen:
            for line in fOpen:
                inner_list = [elt.strip() for elt in line.split(' ')]
                stockIDList.append(inner_list[0])
    if selectScale == 2 :  ##海选
        fileNames=os.listdir(Ccomfunc.src)
        for fileItem in fileNames:
            if os.path.basename(fileItem)[0] in stockIDType: ## 根据文件名的第一个字符区分股票类别 
                stockIDList.append(os.path.splitext(fileItem)[0])
    return stockIDList


## 根据历史日涨幅选股，输入strMonth = "01" strDay ="31"
def selectStockByDayRise(strMonth,strDay):
    stockIDList=makeStockList()
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
        sList=[]
        sList.append(curStock.stockID)
        sList.append(curStock.stockName)
        for sDay in dayStrList:
            indexOfDate=Ccomfunc.getIndexByStrDate(curStock,sDay)
            sList.append( curStock.dayStrList[indexOfDate] )
            sList.append( str(curStock.weekDayList[indexOfDate]) )
            riseRate = -999
            if indexOfDate>=0:
                riseRate = curStock.dayRiseRateCloseArray[indexOfDate] 
            sList.append(str(riseRate))
        if stockID[0]=="8":
            lineWritedList8.append("\t".join(sList))
        else:
            lineWritedList.append("\t".join(sList))
    goalFilePath=strMonth+strDay+'_stockRise.txt'
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    goalFilePath=strMonth+strDay+'_stockRise8.txt'
    Ccomfunc.write2Text(goalFilePath,lineWritedList8)


def printConsumeTime(startClock):
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))

if __name__=="__main__":
   
    startClock=time.clock() ##记录程序开始计算时间
    
    printConsumeTime(startClock)
    startClock=time.clock() ##记录程序开始计算时间
    for i in range(1,31):
        selectStockByDayRise("07",str(i).zfill(2))
   
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


