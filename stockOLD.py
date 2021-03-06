## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import numpy
from scipy.stats.stats import pearsonr

dirData="export"
##定义上证大盘指数List
shLineList=[]
shDateStrList=[]
shPriceOpeningFList=[]
shPriceCloseingFList=[]
shPriceHighestFList=[]
shPriceLowestFList=[]
shTradeVolumeFList=[]
shRiseRateFList=[]  ##涨幅
shWaveRateFLst=[] ##波动涨幅

def readStockSH999999():
    print("\n"+"#"*80)
    print ("当前股票代码:"+"sh999999")
    stockDataFile=os.path.join(dirData,'999999.txt')
    fileOpened=open(stockDataFile,'r')
    lineIndex=0
    for line in fileOpened.readlines():
        lineIndex=lineIndex+1
        splitLine=line.split()
        if line!="" and lineIndex>=3 and len(splitLine)>=6:
            shLineList.append(line)
            shDateStrList.append(splitLine[0])
            shPriceOpeningFList.append(float(splitLine[1]))
            shPriceHighestFList.append(float(splitLine[2]))
            shPriceLowestFList.append(float(splitLine[3]))
            shPriceCloseingFList.append(float(splitLine[4]))
            shTradeVolumeFList.append(float(splitLine[5]))
    fileOpened.close()
    print("上证数据读取完毕,数据开始日：\t"+shDateStrList[0]+"数据结束日：\t"+shDateStrList[-1])



##读取指定代码List
lineList=[]
dayStrList=[]
dayPriceOpenFList=[]
priceCloseingFList=[]
dayPriceHighestFList=[]
dayPriceLowestFList=[]
dayTradeVolumeFList=[] ##成交量
turnoverFList=[]  ##成交额
dayRiseRateFList=[]  ##涨幅
dayWaveRateFList=[] ##波动涨幅

def readStockByID(stockID):
    print("\n"+"#"*80)
    stockDataFile=os.path.join(dirData,stockID+'.txt')
##    if stockID.startswith("6"):
##        stockDataFile=os.path.join(dirData,"SH#"+stockID+'.txt')
##    else:
##        stockDataFile=os.path.join(dirData,"SZ#"+stockID+'.txt')
    fileOpened=open(stockDataFile,'r')
    lineIndex=0
    for line in fileOpened.readlines():
        lineIndex=lineIndex+1
        splitLine=line.split()
        if lineIndex==1:
            print(line)
        if line!="" and lineIndex>=3 and len(splitLine)>=5:
            lineList.append(line)
            dayStrList.append(splitLine[0])
            dayPriceOpenFList.append(float(splitLine[1]))
            dayPriceHighestFList.append(float(splitLine[2]))
            dayPriceLowestFList.append(float(splitLine[3]))
            priceCloseingFList.append(float(splitLine[4]))
            dayTradeVolumeFList.append(float(splitLine[5]))
            if len(priceCloseingFList)>=2:
                dayRiseRateFList.append(round(100*(priceCloseingFList[-1]-priceCloseingFList[-2])/priceCloseingFList[-1],2))
                dayWaveRateFList.append(round(100*(dayPriceHighestFList[-1]-dayPriceLowestFList[-2])/priceCloseingFList[-1],2))
            else:
                dayRiseRateFList.append(0)
                dayWaveRateFList.append(0)
    fileOpened.close()
    print("数据读取完毕,数据开始日：\t"+dayStrList[0]+"\t数据结束日：\t"+dayStrList[-1])


##计算按周期计算涨停幅度

lineWrited=[]

def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

def calNatureDays(dateStr1,dateStr2):
    d1= convertDateStr2Date(dateStr1)
    d2= convertDateStr2Date(dateStr2)
    return (d1-d2).days

def getDateOfPrice(price,priceFList,dayStrList):
    indexPrice=priceFList.index(price)
    return dayStrList[indexPrice]


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
## get analysis indexStartDay and indexEndDay by dayStrList
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
## get analysis indexStartDay and indexEndDay by dayStrList
    indexStart=dayStrList.index(dateStrStart)
    indexEnd=dayStrList.index(dateStrEnd)
    print("-"*50)
    print("分析价差和涨幅")
    
    zhenfuFList=[] ## 波动幅度
    zhangdiefuFList=[]  ##涨跌幅
    for i in range(indexStart,indexEnd):
        priceDelta1=(priceCloseingFList[i]-dayPriceOpenFList[i])/priceCloseingFList[i-1]
        priceDelta2=(dayPriceHighestFList[i]-dayPriceLowestFList[i])/priceCloseingFList[i-1]
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
    print("涨跌幅超过5%:\t"+str(len(zhangdiefuFList))+"\t起始日期是："+strDate)


###连续交易日幅度###
def analysisConsecutive(stockID,dateStrStart,dateStrEnd,numConsecutiveTradeDays,fScale):
## get analysis indexStartDay and indexEndDay by dayStrList
    indexStart=dayStrList.index(dateStrStart)
    indexEnd=dayStrList.index(dateStrEnd)
    print("-"*50)
    print("连续"+str(numConsecutiveTradeDays)+"个交易日幅度超过"+str(fScale))
    
    waveFList=[] ## 波动幅度
    for i in range(indexStart,indexEnd):
        priceDelta1=(priceCloseingFList[i-numConsecutiveTradeDays]-priceCloseingFList[i])/priceCloseingFList[i-numConsecutiveTradeDays]
        if abs(priceDelta1)>=fScale:
            waveFList.append(i)
    strDate=""
    for item in waveFList:
        strDate=strDate+dayStrList[item]+"\t"
    print("振幅超过比例天数:\t"+str(len(waveFList))+"\t起始日期是："+strDate)

    

if __name__=="__main__":
    print("\n"+"#"*80)
    print ("股市有风险，股市有无穷的机会，股市需要耐心，股市态度要认真。")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
    
    goalFilePath='result.txt'

    dataPath=u"Market" ##大盘指数数据目录

    iDaysPeriodUser=300
    readStockSH999999()
    dateStrStart=shDateStrList[-iDaysPeriodUser-1]
    dateStrEnd=shDateStrList[-1]
    analysisDate(dateStrStart,dateStrEnd,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    print ("正在进行大盘时空分析：")
    findPeak(10,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    findPeak(30,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    findPeak(60,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    findPeak(90,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    findPeak(120,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    findPeak(180,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    findPeak(240,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    findPeak(300,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)

    stockID="600000"
    readStockByID(stockID)

  ##  highAndlowPrice(stockID,[iDaysPeriodUser,30,60,120])
    for item in [iDaysPeriodUser,30,60,120]:
        dateStrStart=dayStrList[-item-1]
        dateStrEnd=dayStrList[-1]
        print("\n"+"$"*80)
        analysisDate(dateStrStart,dateStrEnd,dayStrList,dayPriceOpenFList,dayPriceHighestFList,dayPriceLowestFList,priceCloseingFList)
        ##分析单个交易日的波动幅度和振动
        analysisScale(stockID,dateStrStart,dateStrEnd)
        numConsecutiveTradeDays=5
        fScale=0.1
        ##分析连续交易日的价差
        analysisConsecutive(stockID,dateStrStart,dateStrEnd,numConsecutiveTradeDays,fScale)
    
    print ("正在进行时空分析：")
    findPeak(30,dayStrList,dayPriceOpenFList,dayPriceHighestFList,dayPriceLowestFList,priceCloseingFList)
    findPeak(60,dayStrList,dayPriceOpenFList,dayPriceHighestFList,dayPriceLowestFList,priceCloseingFList)
    findPeak(90,dayStrList,dayPriceOpenFList,dayPriceHighestFList,dayPriceLowestFList,priceCloseingFList)
    findPeak(120,dayStrList,dayPriceOpenFList,dayPriceHighestFList,dayPriceLowestFList,priceCloseingFList)
    findPeak(180,dayStrList,dayPriceOpenFList,dayPriceHighestFList,dayPriceLowestFList,priceCloseingFList)

    print ("分析连续交易日情况：")
    contiveTradeDaysAnalysis(5,dayStrList,dayRiseRateFList)


    ##分析连续上涨交易日和连续下跌交易日的成交量对比

    fileWrited=open(goalFilePath,'w')
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    
    ##与大盘同步性分析
    print("与大盘同步性分析")
    numOfTradeDays=200
    analysisSynchronization(stockID,dayStrList[-numOfTradeDays],dayStrList[-1])


    print ("分析近期走势：")
    numOfTradeDays=30
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
    raw_input()


