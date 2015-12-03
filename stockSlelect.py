# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Cstock
import Ccomfunc
import pdb
##计算按周期计算涨停幅度

##选票的条件

##技术选股的条件
##1 弱势的反弹力度
##2 目标价位，支撑价位。

##给出两个交易日期，计算两个交易日的涨幅
def calRiseRateBetween2Date(dateStr,interval):
    ##key is dateStr的指数寻找，是不是交易日，如果找不到怎么办？
    ##判断datestr是否有数据？
    ##如果没有，日期+1，再判断，再没有再+1
    stockIDList=[]
    if len(stockIDList)==0:
        fileNames=os.listdir(Ccomfunc.dirHisData)
        for fileItem in fileNames:
            ##根据字头选择文件 上证6 深圳 0 板块指8 创业板 3
            if os.path.basename(fileItem).startswith("6") or os.path.basename(fileItem).startswith("0") :
                stockIDList.append(os.path.splitext(fileItem)[0])
    lineWritedList=[]
    
    for stockID in stockIDList:
        ##读取股票代码，存储在curStock里
        curStock=Cstock.Stock(stockID,Ccomfunc.dirHisData)
        curStock.list2array()
        indexOfDate=Ccomfunc.getIndexByStrdate(curStock,dateStr)
#        pdb.set_trace()

        ##减少运算量把停牌暴涨的删除了，另外 去掉数组越界的
        if indexOfDate<0:
            pass
        elif len(curStock.dayStrList)<indexOfDate+interval:
            pass
        elif (curStock.dateList[indexOfDate+interval]-curStock.dateList[indexOfDate]).days>interval*2: ##减少运算量把停牌暴涨的删除了
            pass
        else:
            sList=[]
            sList.append(curStock.stockID)
            sList.append(curStock.stockName)
            sList.append(curStock.dayStrList[indexOfDate])
            sList.append(curStock.dayStrList[indexOfDate+interval])
            rise= 100*(curStock.dayPriceClosedFList[indexOfDate+interval]-curStock.dayPriceClosedFList[indexOfDate])/curStock.dayPriceClosedFList[indexOfDate]
            sList.append(str(round(rise,2)))
            lineWritedList.append("\t".join(sList))

    goalFilePath='_result.txt'
    Ccomfunc.write2Text(goalFilePath,lineWritedList)

## 根据指数板块月涨幅选股
def selectStockByMonthRise():
    stockIDList=[]
    if len(stockIDList)==0:
        fileNames=os.listdir(Ccomfunc.dirHisData)
        for fileItem in fileNames:
            ##根据字头选择文件 上证6 深圳 0 板块指8 创业板 3
            if os.path.basename(fileItem).startswith("8") or os.path.basename(fileItem).startswith("9") :
                stockIDList.append(os.path.splitext(fileItem)[0])
    
   
    print ("正在根据条件筛选股票：")
    ##分析板块指数月度数据的涨幅，进行股票板块筛选，这是周期性行情选择的一个主要方法
    lineWritedList=[]
    monthStrList=["201112","201212","201312","201412"]
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
    goalFilePath='result.txt'
    Ccomfunc.write2Text(goalFilePath,lineWritedList)

if __name__=="__main__":
   
    startClock=time.clock() ##记录程序开始计算时间

   #lineWritedList=selectStockByMonthRise() 
    
    lineWritedList=calRiseRateBetween2Date("2013/12/04",10) 
    
    ##分析寻找涨幅最大板块中，当月涨幅最大的个数
    
    ##分析寻找涨幅最大板块中，连续3-5个交易日涨幅最大的个股
   
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


