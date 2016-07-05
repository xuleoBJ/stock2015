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

   
##给出dateStr 交易日,interval 交易日间隔，计算两个交易日的涨幅
def selectStockByRiseRateBetween2Date(inputMDDateStart,inputMDDateEnd,yearList=[2016,2015,2014,2013,2012,2011,2010],selectScale=2):
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
    goalFilePath=os.path.join( Ccomfunc.resultDir,inputMDDateStart.replace("/","")+"-"+inputMDDateEnd.replace("/","")+u'_stockSelect股票.txt')
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    goalFilePath=os.path.join( Ccomfunc.resultDir,inputMDDateStart.replace("/","")+"-"+inputMDDateEnd.replace("/","")+u'_stockSelect板块.txt')
    Ccomfunc.write2Text(goalFilePath,lineWritedList8)


def printConsumeTime(startClock):
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))

if __name__=="__main__":
   
    startClock=time.clock() ##记录程序开始计算时间
    
    selectStockByRiseRateBetween2Date("07/01","07/10") 
    selectStockByRiseRateBetween2Date("07/11","07/20") 
    selectStockByRiseRateBetween2Date("07/21","07/31") 
    selectStockByRiseRateBetween2Date("08/01","08/10") 
    selectStockByRiseRateBetween2Date("08/11","08/20") 
    selectStockByRiseRateBetween2Date("08/21","08/31") 
   
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


