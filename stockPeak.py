# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import sys
import Cstock
import Ccomfunc
import trendAna


stockID="999999"


##分析不同周期的高点及幅度

def getDateOfPrice(price,priceFList,dayStrList):
    indexPrice=priceFList.index(price)
    return dayStrList[indexPrice]

def findPeakPrice(dayPeriod,curDateStrList,curPriceOpenFList,curPriceHighestFList,curPriceLowestFList,curPriceClosedFList):
    print('进行价格峰值分析，分析周期(�?:'+str(dayPeriod))
    goalFilePath=os.path.join(resultDir,stockID+"_"+str(dayPeriod)+'_peakAnalysisPrice.txt') ##输出文件�?
    lineWritedList=[]

    lineWritedList.append('-'*50)
    lineWritedList.append('价格峰值分析分析周�?�?:'+str(dayPeriod))
    lineWritedList.append("日期"+"\t距上次峰值交易日个数\t"+"\t距上次峰值自然日个数\t"+"\t局部高�?低点\t"+"浮动幅度%:\t")
   
    ##变量 用于计算交易日间�?
    d1=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    standValue=100
    daySpanLast=10 ## record last span dayPeriod
    indexLast=1
    dayPeriod=int(dayPeriod/2) ##周期内最�?用半周期前后算，i循环�?比较当日是否是前后半周期的极�?
    for i in range(dayPeriod,len(curDateStrList)):
        ##如果i前后的dayPeriod满足周期 ,i后面的交易日不满足半周期 就用else�?
        max_value = -999
        max_index = 0
        if i<len(curDateStrList)-dayPeriod:
            ##get the highest price of curStock in a period
            max_value = max(curPriceHighestFList[i-dayPeriod:i+dayPeriod])
            max_index = curPriceHighestFList.index(max_value)
        else:
            max_value = max(curPriceHighestFList[i-dayPeriod:])
            max_index = curPriceHighestFList.index(max_value)
            ## write to  file when  the max_index equals to i or pass 
        if max_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            daySpanLast=dayPeriod if daySpanLast==0 else daySpanLast
            riseRate=-999
            if standValue!=0:
                riseRate=round((max_value-standValue)/standValue,3)*100
            lineWritedList.append(curDateStrList[i]+"\t"+str(max_index-indexLast)+"\t"+str(daysSpan)+"\t" \
                    +str(curPriceHighestFList[i])+"\t"+str(riseRate)+"\t")
            d1=d2
            indexLast=max_index
            standValue=max_value
            daySpanLast=daysSpan
           
        min_value = 999 
        min_index = 0
        if i<len(curDateStrList)-dayPeriod:
            min_value = min(curPriceLowestFList[i-dayPeriod:i+dayPeriod])
            min_index = curPriceLowestFList.index(min_value)
        else:
            min_value = min(curPriceLowestFList[i-dayPeriod:])
            min_index = curPriceLowestFList.index(min_value)
        if min_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            riseRate=-999
            if standValue!=0:
                riseRate=round((min_value-standValue)/standValue,3)*100
            lineWritedList.append(curDateStrList[i]+"\t"+str(min_index-indexLast)+"\t"+str(daysSpan)+"\t" \
                    +str(curPriceLowestFList[i])+"\t"+str(riseRate)+"\t")
            d1=d2
            indexLast=min_index
            standValue=min_value
            daySpanLast=daysSpan
    ## deal the last day
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[-1])
    daysSpan=(d2-d1).days
    daySpanLast=dayPeriod if daySpanLast==0 else daySpanLast
    lineWritedList.append(curDateStrList[-1]+"\t" +str(len(curDateStrList)-indexLast)+"\t"+str(daysSpan)+"\t" \
            +str(curPriceClosedFList[-1])+"\t"+str(round((curPriceClosedFList[-1]-standValue)/standValue,3)*100))
    Ccomfunc.write2Text(goalFilePath,lineWritedList) 

def findPeakVolume(dayPeriod,curDateStrList,curTradeVolumeFList):
    print('进行成交量峰值分析，分析周期(�?:'+str(dayPeriod))
    goalFilePath=os.path.join(resultDir,stockID+"_"+str(dayPeriod)+'_peakAnalysisVolume.txt') ##输出文件�?
    lineWritedList=[]
    lineWritedList.append('-'*50)
    lineWritedList.append('成交量峰值分析周�?�?:'+str(dayPeriod))
    lineWritedList.append("日期"+"\t局部高�?低点(万手)\t"+"\t距上次峰值交易日个数\t"+"\t距上次峰值自然日个数\t"+"\t浮动幅度%:\t")

    d1=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    standValue=100
    indexLast=1
    dayPeriod=dayPeriod/2
    for i in range(dayPeriod,len(curDateStrList)-dayPeriod):
        max_value = max(curTradeVolumeFList[i-dayPeriod:i+dayPeriod])
        max_index = curTradeVolumeFList.index(max_value)
        if max_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWritedList.append(curDateStrList[i]+"\t"+str(curTradeVolumeFList[i])+"\t"+str(max_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((max_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=max_index
            standValue=max_value
           
        min_value = min(curTradeVolumeFList[i-dayPeriod:i+dayPeriod])
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
    Ccomfunc.write2Text(goalFilePath,lineWritedList) 

def findPeakTurnover(dayPeriod,curDateStrList,curTurnover):
    print('进行交易额峰值分析，分析周期(�?:'+str(dayPeriod))
    lineWritedList.append('-'*50)
    lineWritedList.append('行交易额峰值分析周�?�?:'+str(dayPeriod))
    lineWritedList.append("日期"+"\t局部高�?低点(亿元)\t"+"\t距上次峰值交易日个数\t"+"\t距上次峰值自然日个数\t"+"\t浮动幅度%:\t")
    d1=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    standValue=100
    indexLast=1
    dayPeriod=dayPeriod/2
    for i in range(dayPeriod,len(curDateStrList)-dayPeriod):
        max_value = max(curTurnover[i-dayPeriod:i+dayPeriod])
        max_index = curTurnover.index(max_value)
        if max_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWritedList.append(curDateStrList[i]+"\t"+str(round(curTurnover[i]/10000,1))+"\t"+str(max_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((max_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=max_index
            standValue=max_value
           
        min_value = min(curTurnover[i-dayPeriod:i+dayPeriod])
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

def analysisDate(dateStrStart,dateStrEnd,curDateStrList,curPriceOpenFList,curPriceHighestFList,curPriceLowestFList,curPriceClosedFList):
## get analysis indexStartDay and indexEndDay by dayStrList
    indexStart=curDateStrList.index(dateStrStart)
    indexEnd=curDateStrList.index(dateStrEnd)
    print("-"*50)
    print("分析周期(交易�?�?:\t"+str(indexEnd-indexStart)+"起始日期:\t"+curDateStrList[indexStart]+"\t结束日期:"+curDateStrList[indexEnd])
    
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
    print("上个最值距离今天的自然日个�?�?:\t"+str(natureDaysNumFromLastPeak2Today.days))
    print("最高点出现与最低点出现交易日个�?�?:\t"+str(1+curPriceHighestFList.index(curPriceHighest)-curPriceLowestFList.index(curPriceLowest)))
    daySpan=calNatureDays(datePriceHighest,datePriceLowest)
    print("最高点出现与最低点出现自然日个�?�?:\t"+str(daySpan))
    print("最高点/最低点:\t"+str(round(curPriceHighest/curPriceLowest,2)))

def analysisScale(stockID,dateStrStart,dateStrEnd):
## get analysis indexStartDay and indexEndDay by dayStrList
    indexStart=dayStrList.index(dateStrStart)
    indexEnd=dayStrList.index(dateStrEnd)
    print("-"*50)
    print("分析价差和涨�?)
    
    zhenfuFList=[] ## 波动幅度
    zhangdiefuFList=[]  ##涨跌�?
    for i in range(indexStart,indexEnd):
        priceDelta1=(dayPriceClosedFList[i]-dayPriceOpenFList[i])/dayPriceClosedFList[i-1]
        priceDelta2=(dayPriceHighestFList[i]-dayPriceLowestFList[i])/dayPriceClosedFList[i-1]
        if priceDelta1>=0.05:
            zhenfuFList.append(i)
        if abs(priceDelta2)>=0.05:
            zhangdiefuFList.append(i)
    strDate=""
    for item in zhenfuFList:
        strDate=strDate+dayStrList[item]+"\t"
    print("振幅超过5%天数:\t"+str(len(zhenfuFList))+"\t起始日期是："+strDate)
    strDate=""
    for item in zhangdiefuFList:
        strDate=strDate+dayStrList[item]+"\t"
    print("涨跌幅超�?%:\t"+str(len(zhangdiefuFList))+"\t起始日期是："+strDate)



if __name__=="__main__":
   
    startClock=time.clock() ##记录程序开始计算时�?
    
    ##读取股票代码，存储在curStock�?
    curStock=Cstock.Stock(stockID)

    ##设置分析周期,如果日期大于1000�?年就�?000），否则取最�?
    iDaysPeriodUser=len(curStock.dayStrList) if len(curStock.dayStrList)<=1000 else 1000
    ##起始分析日期 dateStrStart
    dateStrStart=curStock.dayStrList[-iDaysPeriodUser]
    ##终了分析日期 dateStrEnd
    dateStrEnd=curStock.dayStrList[-1]

    print ("正在进行历史时空分析�?)
    for dayPeriod in [3,5,10,20,30,60,90,120,250]:
        resultDir="resultDir"
        if not os.path.exists(resultDir):
            os.makedirs(resultDir)
       
        findPeakPrice(dayPeriod,curStock.dayStrList,curStock.dayPriceOpenFList,curStock.dayPriceHighestFList,curStock.dayPriceLowestFList,curStock.dayPriceClosedFList)
#        findPeakVolume(dayPeriod,curStock.dayStrList,curStock.dayTradeVolumeFList)
#        findPeakTurnover(dayPeriod,curStock.dayStrList,curStock.dayTurnOverFList)
        
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


