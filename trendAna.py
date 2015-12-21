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

   ## 市场评价 
def marketSum(_curStock,index):
    if 1.5<=_curStock.dayRadioLinkOfTradeVolumeArray[index]:
        strVolumeRadio = u"放巨量"
    if 1.1<=_curStock.dayRadioLinkOfTradeVolumeArray[index]<1.5:
        strVolumeRadio = u"放量"
    if 1<_curStock.dayRadioLinkOfTradeVolumeArray[index]<1.1:
        strVolumeRadio = u"微放量"
    if _curStock.dayRadioLinkOfTradeVolumeArray[index]<1:
        strVolumeRadio =u"缩量"
    
    if 0<=_curStock.dayRiseRateArray[index]:
        resultLine =u"上涨"
    if 0>_curStock.dayRiseRateArray[index]:
        resultLine =u"下跌"
    return strVolumeRadio+resultLine

##计算当月的涨幅
def calRiseRateCurrentMonth1st2today(_curStock):
    firstDay=Ccomfunc.first_day_of_month(datetime.date.today())
    indexStart=Ccomfunc.getIndexByDate(_curStock,firstDay)
    indexEnd=Ccomfunc.getIndexByDate(_curStock,datetime.date.today())
    return calRiseRate(_curStock,indexStart,indexEnd)


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

##计算两个交易日直接的涨幅
def calRiseRate(curStock,indexOfDateStart,indexOfDateEnd):
#    print curStock.stockID,indexOfDateStart,indexOfDateEnd
    return 100*(curStock.dayPriceClosedFList[indexOfDateStart]-curStock.dayPriceClosedFList[indexOfDateEnd])/curStock.dayPriceClosedFList[indexOfDateEnd]

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
   print getDateIndexLowestPoint(curStock,-100,-1)


