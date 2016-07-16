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
import CcomDate

##给出dateStr 交易日,找到初始日期的周一，进行计算
def selectStockByDaysInterval(inputMDDateStart,numTradeDay,yearList=[2016,2015,2014,2013,2012,2011,2010],selectScale=2,dirSelect=2):
    stockIDList=getStockIDList.makeStockList(selectScale)
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
                ## 判断datestrStart 是否是周一，如果不是周一，变成周一 
                dateStrStart = CcomDate.getStrDateMonday_of_week(dateStrStart) 
                indexOfStartDate=Ccomfunc.getIndexByStrDate(curStock,dateStrStart)
                indexOfStartDateSH=Ccomfunc.getIndexByStrDate(shStock,dateStrStart)
                
                indexOfEndDate= indexOfStartDate + numTradeDay
                indexOfEndDateSH= indexOfStartDateSH + numTradeDay
                print indexOfStartDate,curStock.dayStrList[indexOfStartDate],indexOfEndDate,curStock.dayStrList[indexOfEndDate]
                if curStock.count>0 and indexOfStartDate>=0 and indexOfEndDate>0:
                    ##保留日期是为了看是否是停牌影响,同时把两个时间日期写到了一起
                    sList.append(curStock.dayStrList[indexOfStartDate].replace('/','')+"-"+curStock.dayStrList[indexOfEndDate].replace('/',''))
                    rise = -999
                    rise = stockTrendAna.calRiseRateClosed(curStock,indexOfStartDate,indexOfEndDate)
                    riseList.append(rise)
                    riseSH = stockTrendAna.calRiseRateClosed(shStock,indexOfStartDateSH,indexOfEndDateSH)
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

			##write 2 different files	
            if stockID[0] not in ["3","6","0"]:
                lineWritedList8.append("\t".join(sList))
            else:
                lineWritedList.append("\t".join(sList))
    outDir = Ccomfunc.dirSyn if dirSelect == 2 else  Ccomfunc.resultDir
    goalFilePath=os.path.join( outDir,inputMDDateStart.replace("/","")+"+"+str(numTradeDay)+u'_stockSelect股票.txt')
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    goalFilePath=os.path.join( outDir,inputMDDateStart.replace("/","")+"+"+str(numTradeDay)+u'_stockSelect板块.txt')
    Ccomfunc.write2Text(goalFilePath,lineWritedList8)
   
##给出dateStr 交易日,interval 交易日间隔，计算两个交易日的涨幅
def selectStockByRiseRateBetween2Date(inputMDDateStart,inputMDDateEnd,yearList=[2016,2015,2014,2013,2012,2011,2010],selectScale=2,dirSelect=2):
    stockIDList=getStockIDList.makeStockList()
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
                    ##保留日期是为了看是否是停牌影响,同时把两个时间日期写到了一起
                    sList.append(curStock.dayStrList[indexOfStartDate].replace('/','')+"-"+curStock.dayStrList[indexOfEndDate].replace('/',''))
                    rise = -999
                    rise = stockTrendAna.calRiseRateClosed(curStock,indexOfStartDate,indexOfEndDate)
                    riseList.append(rise)
                    riseSH = stockTrendAna.calRiseRateClosed(shStock,indexOfStartDateSH,indexOfEndDateSH)
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

			##write 2 different files	
            if stockID[0] not in ["3","6","0"]:
                lineWritedList8.append("\t".join(sList))
            else:
                lineWritedList.append("\t".join(sList))
    outDir = Ccomfunc.dirSyn if dirSelect == 2 else  Ccomfunc.resultDir
    goalFilePath=os.path.join( outDir,inputMDDateStart.replace("/","")+"-"+inputMDDateEnd.replace("/","")+u'_stockSelect股票.txt')
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    goalFilePath=os.path.join( outDir,inputMDDateStart.replace("/","")+"-"+inputMDDateEnd.replace("/","")+u'_stockSelect板块.txt')
    Ccomfunc.write2Text(goalFilePath,lineWritedList8)


def printConsumeTime(startClock):
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))

if __name__=="__main__":
   
    startClock=time.clock() ##记录程序开始计算时间
    
    ##selectStockByDaysInterval("07/11",10) 
    selectStockByRiseRateBetween2Date("07/16","07/20") 
    selectStockByRiseRateBetween2Date("07/20","07/26") 
    selectStockByRiseRateBetween2Date("07/26","07/31") 
   
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


