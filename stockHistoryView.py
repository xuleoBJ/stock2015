# -*- coding: utf-8 -*-  
import os
import shutil
import time
import datetime
import sys
import Cstock
import Ccomfunc
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter  
import candleStickPlot

lineWrited=[]

## 输出股票阶段涨幅

def outputDataByInpurDateStr(curStock,strMDStart="07/05",strMDEnd="07/18"):
    for strYear in [str(iYear) for iYear in range(2010,2017)]:
        indexList=[] 
        strDateStart = strYear + "/" + strMDStart
        strDateEnd = strYear + "/" + strMDEnd
        indexStart = Ccomfunc.getIndexByStrDate(curStock,strDateStart)
        indexEnd =  Ccomfunc.getIndexByStrDate(curStock,strDateEnd)
        indexList=range(indexStart,indexEnd)
        for i in indexList:
           curStock.printLineDateData(i) 
        print "-"*72

def outputDataByWeekNum(curStock,numWeekStart,numWeekEnd,yearList = range(2010,2017)):
    for iYear in yearList:
        ## 获取交易周的周一的字符串
        dateStrStart = "-".join([str(iYear),str(numWeekStart),str(1)])
        dt = datetime.datetime.strptime(dateStrStart, "%Y-%W-%w")
        dateStrStart=dt.strftime("%Y/%m/%d")
        indexOfStartDate=Ccomfunc.getIndexByStrDate(curStock,dateStrStart)

        ## 获取交易周的周五的字符串
        dateStrEnd= "-".join([str(iYear),str(numWeekEnd),str(5)])
        dt = datetime.datetime.strptime(dateStrEnd, "%Y-%W-%w")
        dateStrEnd=dt.strftime("%Y/%m/%d")
        indexOfEndDate=Ccomfunc.getIndexByStrDate(curStock,dateStrEnd)
        indexList=range(indexOfStartDate,indexOfEndDate+1)
        for i in indexList:
           curStock.printLineDateData(i) 
        print "-"*72


if __name__=="__main__":
   
    startClock=time.clock() ##记录程序开始计算时间

    stockID="600713"
    
    ##读取股票代码，存储在curStock里
    curStock=Cstock.Stock(stockID)
    
    ##输出文件名
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    fileWrited.write(stockID+'\n')
    curStock.printHeadLineDateData()
    
    outputDataByWeekNum(curStock,27,28)

    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))



