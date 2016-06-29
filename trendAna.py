# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import sys
import Cstock
import ConfigParser
import Ccomfunc 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
import datetime
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY,YearLocator, MonthLocator

reload(sys)
sys.setdefaultencoding('utf-8')

def UpDownStasticFor(cStock,matchDateIndex,iDayCycle=60):
    print u"起始\t结束\t数up:Ndown\t和up:Sdown\t均值up:Vdown"
    iDay=5
    for i in range(matchDateIndex-iDayCycle,matchDateIndex+1):
        UpDownStastic(cStock,i-iDay,i)
##趋势分析
def UpDownStastic(cStock,indexStart,indexStartEnd):
     ##趋势定义 
     ##跳水定义：收盘价比最高价低1个点，或者最低价比开盘价低1个点定义为一次跳水
     ##爬升定义：收盘价比最低价高1个点，或者最高价比开盘价高1个点定义为盘中有拉升
     ##低开低走和高开高走的情况重复计算了。不过放大效应是好事。
    fValueTrend=2.0
    ListDown=[]
    ListUp=[]
    if cStock.stockID in ["999999","399001","000300"]:
        fValueTrend=1.0
    for i in range(indexStart,indexStartEnd+1):
        deltaCloseHigh = cStock.dayRiseRateCloseArray[i]-cStock.dayRiseRateHighestArray[i]
        deltaLowOpen = cStock.dayRiseRateLowestArray[i]-cStock.dayRiseRateOpenArray[i]
        ##收盘价比最高价低1个点，或者最低价比开盘价低1个点定义为盘中有跳水
        if deltaCloseHigh<=-fValueTrend: 
            ListDown.append(deltaCloseHigh)   
        if deltaLowOpen<=-fValueTrend:
            ListDown.append(deltaLowOpen) 
        ##收盘价比最低价高1个点，或者最高价比开盘价高1个点定义为盘中有拉升
        deltaHighOpen = cStock.dayRiseRateHighestArray[i]-cStock.dayRiseRateOpenArray[i]
        deltaCloseLow = cStock.dayRiseRateCloseArray[i]-cStock.dayRiseRateLowestArray[i]
        if deltaHighOpen>=fValueTrend :
            ListUp.append(deltaHighOpen)
        if deltaCloseLow>=fValueTrend:
            ListUp.append(deltaCloseLow)
    riseRate=-999
    downArray=np.array(ListDown)
    upArray=np.array(ListUp)
    if indexStartEnd<cStock.count-1:
        riseRate=cStock.dayRiseRateCloseArray[indexStartEnd+1]
    print u"{}\t{}\t{}:{}\t{}:{}({})\t{:.2f}:{:.2f}".format(cStock.dayStrList[indexStartEnd], cStock.dayStrList[indexStart],\
            len(upArray),len(downArray),upArray.sum(),downArray.sum(),upArray.sum()+downArray.sum(),upArray.mean(),downArray.mean())

## 根据成交量和涨幅进行市场评价 
def marketSummary(cStock,index):
    if 1.5<=cStock.dayRadioLinkOfTradeVolumeArray[index]:
        strVolumeRadio = u"放巨量"
    if 1.1<=cStock.dayRadioLinkOfTradeVolumeArray[index]<1.5:
        strVolumeRadio = u"放量"
    if 1<cStock.dayRadioLinkOfTradeVolumeArray[index]<1.1:
        strVolumeRadio = u"微放量"
    if cStock.dayRadioLinkOfTradeVolumeArray[index]<1:
        strVolumeRadio =u"缩量"
    
    if 0<=cStock.dayRiseRateCloseArray[index]<0.5:
        resultLine =u"微涨"
    if 0.5<=cStock.dayRiseRateCloseArray[index]<1:
        resultLine =u"上涨"
    if 1<cStock.dayRiseRateCloseArray[index]:
        resultLine =u"大涨"
    if 0>cStock.dayRiseRateCloseArray[index]>=-0.5:
        resultLine =u"微跌"
    if -0.5>cStock.dayRiseRateCloseArray[index]>-1:
        resultLine =u"下跌"
    if -1>cStock.dayRiseRateCloseArray[index]:
        resultLine =u"大跌"

    if cStock.dayPriceClosedArray[index]<=cStock.day5PriceAverageArray[index]:
        resultLine=resultLine+ " 小于MA5"
    else:
        resultLine=resultLine+ " 大于MA5"
    return strVolumeRadio+resultLine

##计算当月的涨幅
def calRiseRateCurrentMonth1st2today(cStock):
    firstDay=Ccomfunc.first_day_of_month(datetime.date.today())
    indexStart=Ccomfunc.getIndexByDate(cStock,firstDay)
    indexEnd=Ccomfunc.getIndexByDate(cStock,datetime.date.today())
    return calRiseRate(cStock,indexStart,indexEnd)

##  分析历年年同期走势
def trendOfMonthHistory(curStock):
    print (u"历年同月涨幅：".format())
    startYear=curStock.dateList[0].year
    today=datetime.date.today()
    currentYear=today.year
    ymList=[]
    riseRateList=[]
    for iYear in range(startYear,currentYear):
        iMonth=today.month
        strYM=str(iYear)+str(iMonth)
        findIndexStrYM=curStock.monthStrList.index(strYM)
        riseOfmonth=curStock.monthRiseRateFList[findIndexStrYM]
        if riseOfmonth>-100:
            ymList.append(strYM)
            riseRateList.append(riseOfmonth)
            print u"{}年{}月涨幅:{}".format(iYear,iMonth,riseOfmonth)
    valueLine='\t'.join(map(str,sorted(riseRateList)))
    _median=np.median(riseRateList[:])
    print( u"历年涨幅:{}\t中位数:{:.2f}".format(valueLine,_median) )
    
    ind = np.arange(len(ymList))    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    barlist = plt.bar(ind, riseRateList[:], width, color='r')
    for i in range(0,len(riseRateList)):
        if riseRateList[i]<0:
            barlist[i].set_color('g')
    plt.ylabel('riseRate(%)')
    plt.title(curStock.stockName+'history month rise')
    plt.xticks(ind + width/2., ymList[:])

    plt.show()

##获得区间的最高点指数
def getDateIndexHighestPoint(curStock,indexOfDateStart,indexOfDateEnd):
    return indexOfDateStart+curStock.dayPriceHighestArray[indexOfDateStart:indexOfDateEnd].argmax()

##获得区间的最低点指数
def getDateIndexLowestPoint(curStock,indexOfDateStart,indexOfDateEnd):
    return indexOfDateStart+curStock.dayPriceHighestArray[indexOfDateStart:indexOfDateEnd].argmin()

##读取curStock，,indexOfDateStart,indexOfDateEnd，计算 两个交易日收盘涨幅
def calRiseRateClosed(curStock,indexOfDateStart,indexOfDateEnd):
    if curStock.dayPriceClosedFList[indexOfDateStart]>0:
        return 100*(curStock.dayPriceClosedFList[indexOfDateEnd]-curStock.dayPriceClosedFList[indexOfDateStart])/curStock.dayPriceClosedFList[indexOfDateStart]
    else:
        return -999

def calRiseRate(dataArray,indexOfDateStart,indexOfDateEnd):
    if dataArray[indexOfDateStart]>0:
        return 100*(dataArray[indexOfDateEnd]-dataArray[indexOfDateStart])/dataArray[indexOfDateStart]
    else:
        return -999


##计算两个交易日直接的涨幅indexOfDate是指数，interValDay是间隔数，-5就是交易日的前5天与今天的涨幅，+3 就是三日后比今天的涨幅，
def calRiseRateInterval(curStock,indexOfDate,intervalDay):
	if indexOfDate+intervalDay<len(curStock.dayPriceClosedFList) and curStock.dayPriceClosedFList[indexOfDate+intervalDay]>0:
            if intervalDay>0: ##后推
                return 100*(curStock.dayPriceClosedFList[indexOfDate+intervalDay]-curStock.dayPriceClosedFList[indexOfDate])/curStock.dayPriceClosedFList[indexOfDate]
            else:    ##前推 
                return 100*(curStock.dayPriceClosedFList[indexOfDate]-curStock.dayPriceClosedFList[indexOfDate+intervalDay])/curStock.dayPriceClosedFList[indexOfDate+intervalDay]
	else:
		return -999
	    
##计算最后一个交易日，interValDay个交易日的比今天的涨幅，interValDay是间隔数，-5就是交易日的前5天与今天的涨幅，+3 就是三日后比今天的涨幅，
def calTrend(curStock,intervalDay):
    if intervalDay<0:
        return 100*(curStock.dayPriceClosedFList[-1]-curStock.dayPriceClosedFList[-1+intervalDay])/curStock.dayPriceClosedFList[-1+intervalDay]
    else:
		return -999

##输出交易日的差额
def printCalTrend(curStock,intervalDay):
    print(str(intervalDay)+u"个交易日日累计涨幅:"+str(round(calTrend(curStock,intervalDay),2))+"%")

if __name__=="__main__":
   stockID="999999"
   curStock=Cstock.Stock(stockID)
   strMonth="07"
   lineWritedList=[]
## 按月统计涨幅 振幅 最大波动幅度，最小波动幅度
   for year in range(2000,2016):
            dateStrStart = str(year)+"/"+strMonth+"/"+"01"
            indexOfStartDate = Ccomfunc.getIndexByStrDate(curStock,dateStrStart)
            dateStrEnd = str(year)+"/"+strMonth+"/"+"31"
            indexOfDateEnd = Ccomfunc.getIndexByStrDate(curStock,dateStrEnd)
            riseRateMonth =  calRiseRateClosed(curStock,indexOfStartDate,indexOfDateEnd)
            lineOut = u"{}年{}月\t{:.2f}".format(year,strMonth,riseRateMonth)
            lineWritedList.append(lineOut)
            print(lineOut)
   
   goalFilePath = "result.txt" 
   Ccomfunc.write2Text(goalFilePath,lineWritedList)
   os.startfile(goalFilePath)

 #  print getDateIndexLowestPoint(curStock,-100,-1)


