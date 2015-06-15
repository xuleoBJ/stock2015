## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import numpy
import Cstock


##计算按周期计算涨停幅度

lineWrited=[]

def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

def calNatureDays(dateStr1,dateStr2):
    d1= convertDateStr2Date(dateStr1)
    d2= convertDateStr2Date(dateStr2)
    return (d1-d2).days

def getDateOfPrice(price,priceFList,dateStrList):
    indexPrice=priceFList.index(price)
    return dateStrList[indexPrice]


def findPeak(days,curDateStrList,curPriceOpeningFList,curPriceHighestFList,curPriceLowestFList,curPriceCloseingFList):
    print('进行峰值分析，分析周期(天):'+str(days))
    lineWrited.append('-'*50)
    lineWrited.append('分析周期(天):'+str(days))
    lineWrited.append("日期"+"\t局部高点/低点\t"+"\t距上次峰值交易日个数\t"+"\t距上次峰值自然日个数\t"+"\t浮动幅度%:\t")
    d1=convertDateStr2Date(curDateStrList[0])
    d2=convertDateStr2Date(curDateStrList[0])
    standValue=100
    indexLast=1
    days=days/2
    for i in range(days,len(curDateStrList)-days):
##        index, value = max(enumerate(curPriceHighestFList[i-days:i+days]), key=operator.itemgetter(1))
        max_value = max(curPriceHighestFList[i-days:i+days])
        max_index = curPriceHighestFList.index(max_value)
        if max_index==i:
            d2=convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWrited.append(curDateStrList[i]+"\t"+str(curPriceHighestFList[i])+"\t"+str(max_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((max_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=max_index
            standValue=max_value
           
        min_value = min(curPriceLowestFList[i-days:i+days])
        min_index = curPriceLowestFList.index(min_value)
        if min_index==i:
            d2=convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWrited.append(curDateStrList[i]+"\t"+str(curPriceLowestFList[i])+"\t"+str(min_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((min_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=min_index
            standValue=min_value
    d2=convertDateStr2Date(curDateStrList[-1])
    daysSpan=(d2-d1).days
    lineWrited.append(curDateStrList[-1]+"\t"+str(curPriceCloseingFList[-1])+"\t"+str(len(curDateStrList)-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((curPriceCloseingFList[-1]-standValue)/standValue,3)*100))


def contiveTradeDaysAnalysis(numDays,curDateStrList,curRiseRateFList):
    lineWrited.append('-'*50)
    lineWrited.append('连续下跌交易日个数:'+str(numDays))
    indexList=[]
    for i in range(0,len(curRiseRateFList)-numDays):
        bFall=0
        for j in range(numDays):
            if curRiseRateFList[i+j]>=0:
                bFall=1
        if bFall==0:
            print curDateStrList[i]
  ##  lineWrited.append(curDateStrList[-1]+"\t"+str(curPriceCloseingFList[-1])+"\t"+str(len(curDateStrList)-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((curPriceCloseingFList[-1]-standValue)/standValue,3)*100))




def analysisDate(dateStrStart,dateStrEnd,curDateStrList,curPriceOpeningFList,curPriceHighestFList,curPriceLowestFList,curPriceCloseingFList):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=curDateStrList.index(dateStrStart)
    indexEnd=curDateStrList.index(dateStrEnd)
    print("-"*50)
    print("分析周期(交易日/天):\t"+str(indexEnd-indexStart)+"\t起始日期:"+curDateStrList[indexStart]+"\t结束日期:"+curDateStrList[indexEnd])
    
    curPriceHighest=max(curPriceHighestFList[indexStart:indexEnd])
    datePriceHighest=getDateOfPrice(curPriceHighest,curPriceHighestFList,curDateStrList)
    print("区间内最高价:\t"+str(curPriceHighest)+"\t出现日期:\t"+datePriceHighest)
    
    curPriceLowest=min(curPriceLowestFList[indexStart:indexEnd])
    datePriceLowest=getDateOfPrice(curPriceLowest,curPriceLowestFList,curDateStrList)
    print("区间内最低价:\t"+str(curPriceLowest)+"\t出现日期:\t"+datePriceLowest)

    natureDaysNumFromLastPeak2Today=-1  
    if datePriceHighest>=datePriceLowest:
        natureDaysNumFromLastPeak2Today=datetime.date.today()-convertDateStr2Date(datePriceHighest)
    else:
        natureDaysNumFromLastPeak2Today=datetime.date.today()-convertDateStr2Date(datePriceLowest)
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
        priceDelta1=(priceCloseingFList[i]-priceOpeningFList[i])/priceCloseingFList[i-1]
        priceDelta2=(priceHighestFList[i]-priceLowestFList[i])/priceCloseingFList[i-1]
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
    print("\n"+"#"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
    
    shStock=Cstock.StockSH()
    
    stockID="601766"
    curStock=Cstock.Stock(stockID)
    
    goalFilePath='result.txt'

    iDaysPeriodUser=300
    dateStrStart=curStock.dateStrList[-iDaysPeriodUser-1]
    dateStrEnd=curStock.dateStrList[-1]

    print ("正在进行时空分析：")
    findPeak(30,curStock.dateStrList,curStock.priceOpeningFList,curStock.priceHighestFList,curStock.priceLowestFList,curStock.priceCloseingFList)
    findPeak(60,curStock.dateStrList,curStock.priceOpeningFList,curStock.priceHighestFList,curStock.priceLowestFList,curStock.priceCloseingFList)
    findPeak(90,curStock.dateStrList,curStock.priceOpeningFList,curStock.priceHighestFList,curStock.priceLowestFList,curStock.priceCloseingFList)
    findPeak(120,curStock.dateStrList,curStock.priceOpeningFList,curStock.priceHighestFList,curStock.priceLowestFList,curStock.priceCloseingFList)
    findPeak(180,curStock.dateStrList,curStock.priceOpeningFList,curStock.priceHighestFList,curStock.priceLowestFList,curStock.priceCloseingFList)


    fileWrited=open(goalFilePath,'w')
    fileWrited.write(stockID+'\n')
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
    raw_input()


