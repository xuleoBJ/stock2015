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
def trendOfMonthHistory(curStock,numOfyear):
    print (u"过去{}年同月涨幅：".format(numOfyear))
    today=datetime.date.today()
    for i in range(1,numOfyear):
        currentYear=today.year-i
        currentMonth=today.month
        strYM=str(currentYear)+str(currentMonth)
        findIndexStrYM=curStock.monthStrList.index(strYM)
        print u"{}年{}月涨幅:{}".format(currentYear,currentMonth,curStock.monthRiseRateFList[findIndexStrYM])
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
   pass 


