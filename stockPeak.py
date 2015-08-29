# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import sys
import Cstock
import Ccomfunc

reload(sys)
sys.setdefaultencoding('utf-8')

##计算按周期计算涨停幅度

lineWritedList=[]

def getDateOfPrice(price,priceFList,dateStrList):
    indexPrice=priceFList.index(price)
    return dateStrList[indexPrice]


def findPeakPrice(days,curDateStrList,curPriceOpeningFList,curPriceHighestFList,curPriceLowestFList,curPriceCloseingFList):
    print('进行价格峰值分析，分析周期(天):'+str(days))
    lineWritedList.append('-'*50)
    lineWritedList.append('价格峰值分析分析周期(天):'+str(days))
    lineWritedList.append("日期"+"\t距上次峰值交易日个数\t"+"\t距上次峰值自然日个数\t"+"\t自然日间隔比例"+"\t局部高点/低点\t"+"浮动幅度%:\t")
    ##
    d1=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    standValue=100
    daySpanLast=10 ## record last span days
    indexLast=1
    days=days/2
    for i in range(days,len(curDateStrList)-days):
##        index, value = max(enumerate(curPriceHighestFList[i-days:i+days]), key=operator.itemgetter(1))
        ##get the highest price of curStock in a period
        max_value = max(curPriceHighestFList[i-days:i+days])
        max_index = curPriceHighestFList.index(max_value)
        ## write to  file when  the max_index equals to i or pass 
        if max_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            daySpanLast=days if daySpanLast==0 else daySpanLast
            lineWritedList.append(curDateStrList[i]+"\t"+str(max_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round(daysSpan/float(daySpanLast),3))+"\t" \
                    +str(curPriceHighestFList[i])+"\t"+str(round((max_value-standValue)/standValue,3)*100)+"\t")
            d1=d2
            indexLast=max_index
            standValue=max_value
            daySpanLast=daysSpan
           
        min_value = min(curPriceLowestFList[i-days:i+days])
        min_index = curPriceLowestFList.index(min_value)
        if min_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWritedList.append(curDateStrList[i]+"\t"+str(min_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round(daysSpan/float(daySpanLast),3))+"\t" \
                    +str(curPriceLowestFList[i])+"\t"+str(round((min_value-standValue)/standValue,3)*100)+"\t")
            d1=d2
            indexLast=min_index
            standValue=min_value
            daySpanLast=daysSpan
    ## deal the last day
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[-1])
    daysSpan=(d2-d1).days
    daySpanLast=days if daySpanLast==0 else daySpanLast
    lineWritedList.append(curDateStrList[-1]+"\t" +str(len(curDateStrList)-indexLast)+"\t"+str(daysSpan)+"\t"+str(round(daysSpan/float(daySpanLast),3))+"\t" \
            +str(curPriceCloseingFList[-1])+"\t"+str(round((curPriceCloseingFList[-1]-standValue)/standValue,3)*100))

def findPeakVolume(days,curDateStrList,curTradeVolumeFList):
    print('进行成交量峰值分析，分析周期(天):'+str(days))
    lineWritedList.append('-'*50)
    lineWritedList.append('成交量峰值分析周期(天):'+str(days))
    lineWritedList.append("日期"+"\t局部高点/低点(万手)\t"+"\t距上次峰值交易日个数\t"+"\t距上次峰值自然日个数\t"+"\t浮动幅度%:\t")

    d1=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    standValue=100
    indexLast=1
    days=days/2
    for i in range(days,len(curDateStrList)-days):
        max_value = max(curTradeVolumeFList[i-days:i+days])
        max_index = curTradeVolumeFList.index(max_value)
        if max_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWritedList.append(curDateStrList[i]+"\t"+str(curTradeVolumeFList[i])+"\t"+str(max_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((max_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=max_index
            standValue=max_value
           
        min_value = min(curTradeVolumeFList[i-days:i+days])
        min_index = curTradeVolumeFList.index(min_value)
        if min_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWritedList.append(curDateStrList[i]+"\t"+str(curTradeVolumeFList[i])+"\t"+str(min_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((min_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=min_index
            standValue=min_value
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[-1])
    daysSpan=(d2-d1).days
    lineWritedList.append(curDateStrList[-1]+"\t"+str(curTradeVolumeFList[-1])+"\t"+str(len(curDateStrList)-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((curTradeVolumeFList[-1]-standValue)/standValue,3)*100))


def findPeakTurnover(days,curDateStrList,curTurnover):
    print('进行交易额峰值分析，分析周期(天):'+str(days))
    lineWritedList.append('-'*50)
    lineWritedList.append('行交易额峰值分析周期(天):'+str(days))
    lineWritedList.append("日期"+"\t局部高点/低点(亿元)\t"+"\t距上次峰值交易日个数\t"+"\t距上次峰值自然日个数\t"+"\t浮动幅度%:\t")
    d1=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    standValue=100
    indexLast=1
    days=days/2
    for i in range(days,len(curDateStrList)-days):
        max_value = max(curTurnover[i-days:i+days])
        max_index = curTurnover.index(max_value)
        if max_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWritedList.append(curDateStrList[i]+"\t"+str(round(curTurnover[i]/10000,1))+"\t"+str(max_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((max_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=max_index
            standValue=max_value
           
        min_value = min(curTurnover[i-days:i+days])
        min_index = curTurnover.index(min_value)
        if min_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWritedList.append(curDateStrList[i]+"\t"+str(round(curTurnover[i]/10000,1))+"\t"+str(min_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((min_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=min_index
            standValue=min_value
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[-1])
    daysSpan=(d2-d1).days
    lineWritedList.append(curDateStrList[-1]+"\t"+str(round(curTurnover[-1]/10000,1))+"\t"+str(len(curDateStrList)-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((curTurnover[-1]-standValue)/standValue,3)*100))

def analysisDate(dateStrStart,dateStrEnd,curDateStrList,curPriceOpeningFList,curPriceHighestFList,curPriceLowestFList,curPriceCloseingFList):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=curDateStrList.index(dateStrStart)
    indexEnd=curDateStrList.index(dateStrEnd)
    print("-"*50)
    print("分析周期(交易日/天):\t"+str(indexEnd-indexStart)+"起始日期:\t"+curDateStrList[indexStart]+"\t结束日期:"+curDateStrList[indexEnd])
    
    curPriceHighest=max(curPriceHighestFList[indexStart:indexEnd])
    datePriceHighest=getDateOfPrice(curPriceHighest,curPriceHighestFList,curDateStrList)
    print("区间内最高价:\t"+str(curPriceHighest)+"出现日期:\t"+datePriceHighest)
    
    curPriceLowest=min(curPriceLowestFList[indexStart:indexEnd])
    datePriceLowest=getDateOfPrice(curPriceLowest,curPriceLowestFList,curDateStrList)
    print("区间内最低价:\t"+str(curPriceLowest)+"出现日期:\t"+datePriceLowest)

    natureDaysNumFromLastPeak2Today=-1  
    if datePriceHighest>=datePriceLowest:
        natureDaysNumFromLastPeak2Today=datetime.date.today()-Ccomfunc.convertDateStr2Date(datePriceHighest)
    else:
        natureDaysNumFromLastPeak2Today=datetime.date.today()-Ccomfunc.convertDateStr2Date(datePriceLowest)
    print("上个最值距离今天的自然日个数(天):\t"+str(natureDaysNumFromLastPeak2Today.days))
    print("最高点出现与最低点出现交易日个数(天):\t"+str(1+curPriceHighestFList.index(curPriceHighest)-curPriceLowestFList.index(curPriceLowest)))
    daySpan=calNatureDays(datePriceHighest,datePriceLowest)
    print("最高点出现与最低点出现自然日个数(天):\t"+str(daySpan))
    print("最高点/最低点:\t"+str(round(curPriceHighest/curPriceLowest,2)))

def analysisScale(stockID,dateStrStart,dateStrEnd):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=dateStrList.index(dateStrStart)
    indexEnd=dateStrList.index(dateStrEnd)
    print("-"*50)
    print("分析价差和涨幅")
    
    zhenfuFList=[] ## 波动幅度
    zhangdiefuFList=[]  ##涨跌幅
    for i in range(indexStart,indexEnd):
        priceDelta1=(priceClosedFList[i]-priceOpeningFList[i])/priceClosedFList[i-1]
        priceDelta2=(priceHighestFList[i]-priceLowestFList[i])/priceClosedFList[i-1]
        if priceDelta1>=0.05:
            zhenfuFList.append(i)
        if abs(priceDelta2)>=0.05:
            zhangdiefuFList.append(i)
    strDate=""
    for item in zhenfuFList:
        strDate=strDate+dateStrList[item]+"\t"
    print("振幅超过5%天数:\t"+str(len(zhenfuFList))+"\t起始日期是："+strDate)
    strDate=""
    for item in zhangdiefuFList:
        strDate=strDate+dateStrList[item]+"\t"
    print("涨跌幅超过5%:\t"+str(len(zhangdiefuFList))+"\t起始日期是："+strDate)



if __name__=="__main__":
    print("\n"+"#"*80)
    print ("股市有风险，股市有无穷的机会，股市需要耐心，股市态度要认真。")
    print ("分析大的趋势和振幅，波峰和波谷。")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
   
    ##读取上证指数数据
    ##shStock=Cstock.StockSH()
    

    ##读取股票代码，存储在curStock里
    stockID="999999"
    curStock=Cstock.Stock(stockID)
    

    ##设置分析周期
    iDaysPeriodUser=800
    ##起始分析日期 dateStrStart
    dateStrStart=curStock.dateStrList[-iDaysPeriodUser-1]
    ##终了分析日期 dateStrEnd
    dateStrEnd=curStock.dateStrList[-1]

    print ("正在进行现状分析：")
    for days in [3,5,10,20,30]:
	 Ccomfunc.printCalTrend(curStock,days)
	   

    print ("正在进行历史时空分析：")
    for days in [5,10,20,30,60,90,120,180,300]:
        resultDir="resultDir"
        if not os.path.exists(resultDir):
            os.makedirs(resultDir)
        goalFilePath=os.path.join(resultDir,stockID+"_"+str(days)+'_峰值周期历史分析.txt') ##输出文件名
        lineWritedList=[]
        findPeakPrice(days,curStock.dateStrList,curStock.priceOpeningFList,curStock.priceHighestFList,curStock.priceLowestFList,curStock.priceClosedFList)
        findPeakVolume(days,curStock.dateStrList,curStock.tradeVolumeFList)
        findPeakTurnover(days,curStock.dateStrList,curStock.turnOverFList)
        fileWrited=open(goalFilePath,'w')
        fileWrited.write(stockID+'\n')
        for line in lineWritedList:
            fileWrited.write(line+'\n')
        fileWrited.close()
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


