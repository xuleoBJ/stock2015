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

##根据量能选择股票
def selectStockByVolume():
    stockIDList=makeStockList()
    lineWritedList=[]
    
    shStock=Cstock.Stock("999999")
    sIDList = []  
    ##类型 1 放巨量 2 三日连续放量 3 三日连续缩量下跌
    for stockID in stockIDList:
        curStock=Cstock.Stock(stockID)
        if curStock.count>0:  ##剔除数据项为空的 
            ##3日缩量下跌
            if curStock.dayRadioLinkOfTradeVolumeArray[-1]<1 and curStock.dayRiseRateArray[-1]<0:
                if curStock.dayRadioLinkOfTradeVolumeArray[-2]<1 and curStock.dayRiseRateArray[-1]<0:
                    if curStock.dayRadioLinkOfTradeVolumeArray[-3]<1 and curStock.dayRiseRateArray[-1]<0:
                        sIDList.append(stockID)
                        sIDList.append("3")
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-3]))
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-2]))
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-1]))
            
            ##3日放量上涨
            if curStock.dayRadioLinkOfTradeVolumeArray[-1]>1 and curStock.dayRiseRateArray[-1]>0:
                if curStock.dayRadioLinkOfTradeVolumeArray[-2]>1 and curStock.dayRiseRateArray[-1]>0:
                    if curStock.dayRadioLinkOfTradeVolumeArray[-3]>1 and curStock.dayRiseRateArray[-1]>0:
                        sIDList.append(stockID)
                        sIDList.append("2")
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-3]))
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-2]))
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-1]))

            ##比较大盘和个股的量能指标选择股票,选择放量的stockID
            if curStock.dayStrList[-1]==shStock.dayStrList[-1]:
                if curStock.dayRadioLinkOfTradeVolumeArray[-1]>=1.5:
                    if curStock.dayRadioLinkOfTradeVolumeArray[-1]-shStock.dayRadioLinkOfTradeVolumeArray[-1]>0.5:
                        sIDList.append(stockID)
                        sIDList.append("1")
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-3]))
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-2]))
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-1]))
            lineWritedList.append("\t".join(sIDList))
    print lineWritedList
    goalFilePath=os.path.join(Ccomfunc.resultDir,'_stockSelect.txt') ##输出文件名
    Ccomfunc.write2Text(goalFilePath,lineWritedList)

##技术选股的条件
##1 弱势的反弹力度
##2 目标价位，支撑价位。

   
##给出dateStr 交易日,interval 交易日间隔，计算两个交易日的涨幅
def selectStockByRiseRateBetween2Date(inputMDDateStart,inputMDDateEnd,yearList=[2015,2014,2013,2012,2011,2010],selectScale=2):
    stockIDList=makeStockList()
    lineWritedList=[]
    lineWritedList8=[]  ##指数为8的单独写出来
    
    shStock=Cstock.Stock("999999")
    for stockID in stockIDList:
        ##读取股票代码，存储在curStock里
        curStock=Cstock.Stock(stockID)
        if curStock.count>0:
            sList = []
            sList.append(curStock.stockID)
            sList.append(curStock.stockName)
            riseList=[]
            riseSHList=[]
            iBig = 0 ##计数器，跟大盘涨幅对比
            for year in yearList:
                dateStrStart=str(year)+"/"+inputMDDateStart
                indexOfStartDate=Ccomfunc.getIndexByStrDate(curStock,dateStrStart)
                indexOfStartDateSH=Ccomfunc.getIndexByStrDate(shStock,dateStrStart)
                dateStrEnd=str(year)+"/"+inputMDDateEnd
                indexOfEndDate=Ccomfunc.getIndexByStrDate(curStock,dateStrEnd)
                indexOfEndDateSH=Ccomfunc.getIndexByStrDate(shStock,dateStrEnd)
                print indexOfStartDate,curStock.dayStrList[indexOfStartDate],indexOfEndDate,curStock.dayStrList[indexOfEndDate]
                if curStock.count>0 and indexOfStartDate>=0 and indexOfEndDate>0:
                    sList.append(curStock.dayStrList[indexOfStartDate])
                    sList.append(curStock.dayStrList[indexOfEndDate])
                    rise = -999
                    rise = trendAna.calRiseRateClosed(curStock,indexOfStartDate,indexOfEndDate)
                    riseList.append(rise)
                    riseSH = trendAna.calRiseRateClosed(shStock,indexOfStartDateSH,indexOfEndDateSH)
                    riseSHList.append(riseSH)
                    ##记录强于大盘的个数
                    if rise>=riseSH:
                        iBig = iBig+1
                    sList.append(str(round(rise,2)))
            sList.append(str(iBig))
            if stockID=="999999":
                sList.append(str(round(np.array(riseSHList).mean(),2)))
            else:
                sList.append(str(round(np.array(riseList).mean(),2)))
				
            if stockID[0]=="8":
                lineWritedList8.append("\t".join(sList))
            else:
                lineWritedList.append("\t".join(sList))
    goalFilePath=os.path.join(Ccomfunc.resultDir,inputMDDateStart.replace("/","")+"-"+inputMDDateEnd.replace("/","")+'_stockSelect.txt') ##输出文件名
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    goalFilePath=os.path.join(Ccomfunc.resultDir,inputMDDateStart.replace("/","")+"-"+inputMDDateEnd.replace("/","")+'_stockSelect8.txt') ##输出文件名
    Ccomfunc.write2Text(goalFilePath,lineWritedList8)

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
            sList.append(sDay)
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
    selectStockByRiseRateBetween2Date("06/01","06/15") 
    printConsumeTime(startClock)
    startClock=time.clock() ##记录程序开始计算时间
    
    selectStockByRiseRateBetween2Date("06/16","06/30") 
    selectStockByRiseRateBetween2Date("07/01","07/15") 
    selectStockByRiseRateBetween2Date("07/16","07/30")  
    case=4
    ##分析寻找涨幅最大板块中，当月涨幅最大的个数
    if case==1:
        selectStockByMonthRise("07") 
    if case==2:
        selectStockByRiseRateBetween2Date("06/01","06/15") 
        selectStockByRiseRateBetween2Date("06/16","06/30") 
        selectStockByRiseRateBetween2Date("07/01","07/15") 
        selectStockByRiseRateBetween2Date("07/16","07/30") 
    if case==3:
        selectStockByVolume()
    if case==4:
        printConsumeTime(startClock)
        startClock=time.clock() ##记录程序开始计算时间
        for i in range(1,31):
            selectStockByDayRise("07",str(i).zfill(2))
   
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


