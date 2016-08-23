# -*- coding: utf-8 -*-
import os
import datetime,time
import ConfigParser
import Cstock
import Ccomfunc
import configOS
import stockPatternRecognition
import stockTradeModel
import stockTrendAna
import ctypes 

if __name__ == "__main__":
 
    startClock=time.clock() ##记录程序开始计算时间
    
    stockID="999999"
    curStock=Cstock.Stock(stockID)
   
    strDate=""

    now = datetime.datetime.now()
    marketStartTime = now.replace(hour=9, minute=30, second=0, microsecond=0) 
    marketEndTime = now.replace(hour=15, minute=00, second=0, microsecond=0)
    
    ##根据时间自动取strDate,开盘之前 以后取昨天，下午三点以前今天
    if strDate=="" and now <= marketEndTime:
        strDate=(datetime.date.today()-datetime.timedelta(days=1)).strftime("%Y/%m/%d")
    if strDate=="" and now >= marketEndTime:
        strDate=datetime.date.today().strftime("%Y/%m/%d")

    matchDateIndex = Ccomfunc.getIndexByStrDate(curStock,strDate)
    print (u"分析日期：{}".format(curStock.dayStrList[matchDateIndex])) 
    print u"技术性风险。"
    ## 连续三日收盘价在5日均线以下
    if curStock.dayPriceClosedArray[matchDateIndex] < curStock.day5PriceAverageArray[matchDateIndex] and \
       curStock.dayPriceClosedArray[matchDateIndex] < curStock.day5PriceAverageArray[matchDateIndex-1] and \
       curStock.dayPriceClosedArray[matchDateIndex] < curStock.day5PriceAverageArray[matchDateIndex-2] :
           print u"连续三日收盘价低于5日均线"
    if curStock.dayPriceLowestArray[matchDateIndex] < curStock.day5PriceAverageArray[matchDateIndex] and \
       curStock.dayPriceLowestArray[matchDateIndex] < curStock.day5PriceAverageArray[matchDateIndex-1] and \
       curStock.dayPriceLowestArray[matchDateIndex] < curStock.day5PriceAverageArray[matchDateIndex-2] :
           print u"连续三日盘中最低点5日均线"
    ## 放巨量大跌
    
    ## 放巨量上涨

    timeSpan=time.clock()-startClock
    
    print u"系统性风险。"
    ## 美股暴跌

    print("Time used(s):",round(timeSpan,2))



