# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Cstock
import Ccomfunc
import pdb
import trendAna
##计算按周期计算涨停幅度

##选票的条件

##技术选股的条件
##1 弱势的反弹力度
##2 目标价位，支撑价位。

##给出dateStr 交易日,interval 交易日间隔，计算两个交易日的涨幅
def calRiseRateBetween2Date(myStrInput,interval):
    stockIDList=["999999","399001"]
    fileNames=os.listdir(Ccomfunc.src)
    for fileItem in fileNames:
        ##根据字头选择文件 上证6 深圳 0 板块指8 创业板 3
        if os.path.basename(fileItem).startswith("6") or os.path.basename(fileItem).startswith("0") :
            stockIDList.append(os.path.splitext(fileItem)[0])
    lineWritedList=[]
    
    shStock=Cstock.Stock("999999")
    shStock.list2array()
    for stockID in stockIDList:
        ##读取股票代码，存储在curStock里
        curStock=Cstock.Stock(stockID)
        curStock.list2array()
        sList = []
        sList.append(curStock.stockID)
        sList.append(curStock.stockName)
        iBig = 0 ##计数器，跟大盘涨幅对比
        for year in [2010,2011,2012,2013,2014]:
            dateStr=str(year)+"/"+myStrInput
            print dateStr
            indexOfDate=Ccomfunc.getIndexByStrdate(curStock,dateStr)
    #        pdb.set_trace()
            ##减少运算量把停牌暴涨的删除了，另外 去掉数组越界的
            if indexOfDate<0:
                pass
            elif len(curStock.dayStrList)<=indexOfDate+interval:
                pass
            elif (curStock.dateList[indexOfDate+interval]-curStock.dateList[indexOfDate]).days>interval*2: ##减少运算量把停牌暴涨的删除了
                pass
            else:
                sList.append(curStock.dayStrList[indexOfDate])
                sList.append(curStock.dayStrList[indexOfDate+interval])
                rise = trendAna.calRiseRate(curStock,indexOfDate,indexOfDate+interval)
                riseSH = trendAna.calRiseRate(shStock,indexOfDate,indexOfDate+interval)
                sList.append(str(round(rise,2)))
                ##记录强于大盘的个数
                if rise>=riseSH:
                    iBig = iBig+1
        sList.append(str(iBig))
        lineWritedList.append("\t".join(sList))
    goalFilePath=os.path.join(Ccomfunc.resultDir,'_stockSelect.txt') ##输出文件名
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
    
    lineWritedList=calRiseRateBetween2Date("12/10",15) 
    
    ##分析寻找涨幅最大板块中，当月涨幅最大的个数
    
    ##分析寻找涨幅最大板块中，连续3-5个交易日涨幅最大的个股
   
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


