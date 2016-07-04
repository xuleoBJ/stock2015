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
	
    print ("条件筛选股票："+strMonth+strDay)
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

## 根据指数板块月涨幅选股
def selectStockByMonthRise(strMonth):
    stockIDList=makeStockList()
    print ("正在根据条件筛选股票：")
    ##分析板块指数月度数据的涨幅，进行股票板块筛选，这是周期性行情选择的一个主要方法
    lineWritedList=[]
    monthStrList=[ strMonth+ele for ele in ["2011","2012","2013","2014","2015"]]
    for stockID in stockIDList:
        ##读取股票代码，存储在curStock里
        curStock=Cstock.Stock(stockID)
        sList=[]
        sList.append(curStock.stockID)
        sList.append(curStock.stockName)
        for sMonth in monthStrList:
            sList.append(sMonth)
            _riseRateMonth="-999"
            for i in range(len(curStock.monthStrList)):
                if curStock.monthStrList[i].endswith(sMonth):
                    _riseRateMonth=str(curStock.monthRiseRateFList[i])
            sList.append(_riseRateMonth)
        lineWritedList.append("\t".join(sList))
    goalFilePath=strMonth+'_stockRise.txt'
    Ccomfunc.write2Text(goalFilePath,lineWritedList)

def printConsumeTime(startClock):
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))

if __name__=="__main__":
   
    startClock=time.clock() ##记录程序开始计算时间
    
    case=2
    ##分析寻找涨幅最大板块中，当月涨幅最大的个数
    if case==1:
        selectStockByMonthRise("07") 
    if case==2:
        selectStockByRiseRateBetween2Date("06/01","06/10") 
        selectStockByRiseRateBetween2Date("06/01","06/15") 
        selectStockByRiseRateBetween2Date("06/16","06/30") 
    if case==3:
        selectStockByVolume()
    if case==4:
        printConsumeTime(startClock)
        startClock=time.clock() ##记录程序开始计算时间
        for i in range(1,31):
            selectStockByDayRise("07",str(i).zfill(2))
   
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


