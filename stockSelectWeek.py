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


##selectScale=1 从文本文件stockIDList.txt 读取 =2，海选 ,dirSelect=1 选择结果输出文件夹
def selectStockByRiseRateByWeek(numWeekList,yearList=[2017,2016,2015,2014,2013,2012,2011,2010],selectScale=2,dirSelect=2):
    stockIDList=getStockIDList.makeStockList(selectScale)
    
    shStock=Cstock.Stock("999999")
    for numWeek in numWeekList:
        lineWritedList=[]
        lineWritedList8=[]  ##指数为8的单独写出来
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
                for iYear in yearList:
                    ## 获取交易周的周一的字符串
                    dateStrStart = "-".join([str(iYear),str(numWeek),str(1)])
                    dt = datetime.datetime.strptime(dateStrStart, "%Y-%W-%w")
                    dateStrStart=dt.strftime("%Y/%m/%d")
                    indexOfStartDate=Ccomfunc.getIndexByStrDate(curStock,dateStrStart)
                    indexOfStartDateSH=Ccomfunc.getIndexByStrDate(shStock,dateStrStart)

                    ## 获取交易周的周五的字符串
                    dateStrEnd= "-".join([str(iYear),str(numWeek),str(5)])
                    dt = datetime.datetime.strptime(dateStrEnd, "%Y-%W-%w")
                    dateStrEnd=dt.strftime("%Y/%m/%d")
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

                ##write 2 different files	
                if stockID[0] not in ["3","6","0"]:
                    lineWritedList8.append("\t".join(sList))
                else:
                    lineWritedList.append("\t".join(sList))
        outDir = Ccomfunc.dirSyn if dirSelect == 2 else  Ccomfunc.resultDir
        if os.path.exists(outDir) == False:
            outDir =  Ccomfunc.resultDir
        goalFilePath=os.path.join( outDir , "week"+str(numWeek)+u'_stockSelect股票.txt')
        Ccomfunc.write2Text(goalFilePath,lineWritedList)
        goalFilePath=os.path.join( outDir , "week"+str(numWeek)+u'_stockSelect板块.txt')
        Ccomfunc.write2Text(goalFilePath,lineWritedList8)


def printConsumeTime(startClock):
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))

if __name__=="__main__":
   
    startClock=time.clock() ##记录程序开始计算时间
    
    selectStockByRiseRateByWeek(range(5,10)) 
   
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


