# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import sys
import Cstock
import ConfigParser
import Ccomfunc 

reload(sys)
sys.setdefaultencoding('utf-8')


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
    for iYear in range(startYear,currentYear):
        iMonth=today.month
        strYM=str(iYear)+str(iMonth)
        findIndexStrYM=curStock.monthStrList.index(strYM)
        print u"{}年{}月涨幅:{}".format(iYear,iMonth,curStock.monthRiseRateFList[findIndexStrYM])

##获得区间的最高点指数
def getDateIndexHighestPoint(curStock,indexOfDateStart,indexOfDateEnd):
    return indexOfDateStart+curStock.dayPriceHighestArray[indexOfDateStart:indexOfDateEnd].argmax()

##获得区间的最低点指数
def getDateIndexLowestPoint(curStock,indexOfDateStart,indexOfDateEnd):
    return indexOfDateStart+curStock.dayPriceHighestArray[indexOfDateStart:indexOfDateEnd].argmin()

##计算两个交易日直接的涨幅
def calRiseRate(curStock,indexOfDateStart,indexOfDateEnd):
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
   curStock.list2array()
   print getDateIndexLowestPoint(curStock,-100,0)


