# -*- coding: utf-8 -*-
import os
import datetime,time
import ConfigParser
import Cstock
import Ccomfunc
import configOS
import stockPatternRecognition
import stockTecSet
import volumeEnerge
import trendAna
import ctypes 

from PyQt4 import QtGui # Import the PyQt4 module we'll need
from PyQt4.QtGui import *


##需要从配置文件中读取不同周期的极值，以便计算压力位和支撑位
def calResistLine(cyclePeriod,keyPoint):
    resistLine=cycleLow+(cycleHigh-cycleLow)*keyPoint
    return resistLine

def calGDG():
    print(u"分析两市总市值和GDP的关系")
    gdp2014=63.6
    ##此处应该设计必须成输入！
    AB_SH=30.0
    AB_SZ=21.7
    print (u"股市与GDP值比{:.2f}".format((AB_SH+AB_SZ)/gdp2014))

def WarnBigEvent():
    ctypes.windll.user32.MessageBoxA(0, "2016-1-8 Big Share Sells!", "infor", 1)

def main(stockID,strDate=Ccomfunc.defaultDateInputStr()):
    ##近期事务提醒，希望建立数据库
    WarnBigEvent() 
    curStock=Cstock.Stock(stockID)
    
    matchDateIndex = Ccomfunc.getIndexByStrDate(curStock,strDate)
    print (u"分析日期：{}".format(curStock.dayStrList[matchDateIndex]))

    print(u"-"*72)
    print(u"近期市场分析：")
    headLine=u"日期\t星期\t涨幅\t最高\t最低\t量能\t描述"
    print(headLine)
    for i in range(matchDateIndex-5,matchDateIndex+1):
        weekDay = curStock.dateList[i].isoweekday()
        marketSummaryStr = trendAna.marketSummary(curStock,i)
        print(u"{} {}\t{:.2f}%({:.2f})\t{:.1f}({:.2f}%)\t{:.1f}({:.2f}%)\t{}\t{}".format(curStock.dayStrList[i], weekDay , \
                curStock.dayRiseRateFList[i],curStock.dayPriceClosedFList[i],\
                curStock.dayPriceHighestArray[i],curStock.dayRiseRateHighestArray[i],\
                curStock.dayPriceLowestFList[i],curStock.dayRiseRateLowestArray[i],\
                curStock.dayRadioLinkOfTradeVolumeFList[i], marketSummaryStr))
    
    ## 均价分析
    print (u"-"*72)
    print (u"均价分析：")
    headLine=u"\t3日\t5日\t10日\t20日"
    print(headLine)
    print(u"价 {}\t{}\t{}\t{}".format(curStock.day3PriceAverageArray[matchDateIndex],curStock.day5PriceAverageArray[matchDateIndex],\
            curStock.day10PriceAverageArray[matchDateIndex],curStock.day20PriceAverageArray[matchDateIndex]) )
    print(u"量 {}\t{}\t{}\t{}".format(curStock.day3TradeVolumeArray[matchDateIndex],curStock.day5TradeVolumeArray[matchDateIndex],\
            curStock.day10TradeVolumeArray[matchDateIndex],curStock.day20TradeVolumeArray[matchDateIndex]) )
    print (u"-"*72)
    
    ## 1. 首先要做趋势分析！趋势分为长期，中期，短期趋势
    print(u"1-时空趋势分析")
    print (u"-"*72)
    print (u"正在进行时间趋势分析：")
    
    headline=u"周期(日) 高(低)点\t日期\t交易日数\t涨幅%\t量能比"
    print (headline)
    for period in [5,10,20,30,60,120]:
        indexHighPoint=matchDateIndex-period+curStock.dayPriceHighestArray[matchDateIndex-period:matchDateIndex+1].argmax()
        riseHighcurrent=-999
        if curStock.dayPriceHighestFList[indexHighPoint]!=0:
            riseHighcurrent=100*(curStock.dayPriceClosedFList[matchDateIndex]-curStock.dayPriceHighestFList[indexHighPoint])/curStock.dayPriceHighestFList[indexHighPoint]
        rateHighTradeVolumecurrent=-999
        if curStock.dayTradeVolumeFList[indexHighPoint]!=0:
            rateHighTradeVolumecurrent=curStock.dayTradeVolumeFList[matchDateIndex]/curStock.dayTradeVolumeFList[indexHighPoint]
        indexLowPoint=matchDateIndex-period+curStock.dayPriceLowestArray[matchDateIndex-period:matchDateIndex+1].argmin()
        riseLowcurrent=-999
        if curStock.dayPriceLowestFList[indexHighPoint]!=0:
            riseLowcurrent=100*(curStock.dayPriceClosedFList[matchDateIndex]-curStock.dayPriceLowestFList[indexLowPoint])/curStock.dayPriceLowestFList[indexLowPoint]
        rateLowTradeVolumecurrent=-999
        if curStock.dayTradeVolumeFList[indexHighPoint]!=0:
            rateLowTradeVolumecurrent=curStock.dayTradeVolumeFList[matchDateIndex]/curStock.dayTradeVolumeFList[indexLowPoint]
        print(u"{}日\t{}\t{}\t{}\t{:.2f}\t{:.2f}".format(period,curStock.dayPriceHighestFList[indexHighPoint], \
                curStock.dayStrList[indexHighPoint],matchDateIndex-indexHighPoint,riseHighcurrent,rateHighTradeVolumecurrent))
        print(u"{}日\t{}\t{}\t{}\t{:.2f}\t{:.2f}".format(period,curStock.dayPriceLowestFList[indexLowPoint], \
                curStock.dayStrList[indexLowPoint],matchDateIndex-indexLowPoint,riseLowcurrent,rateLowTradeVolumecurrent))

    ## 时空分析,关键支撑分析
    print(u"-"*72)
    print(u"关键点位提示分析：")
    print(u"-"*72)
    headline=u"周期(日)幅度\t低点\t高点\t点位"
    print (headline)
    for period in [20,60,120,180]:
        cycleHigh=curStock.dayPriceHighestArray[matchDateIndex-period:].max()
        cycleLow=curStock.dayPriceLowestArray[matchDateIndex-period:].min()
        for keyPoint in [0.33,0.5,0.825]:
            resistLinePoint=cycleLow+(cycleHigh-cycleLow)*keyPoint
            resultLine=u"{}日\t{}\t{}\t{}\t{:.2f}".format(period,keyPoint,cycleLow,cycleHigh,resistLinePoint)
            if 0.99<=curStock.dayPriceClosedFList[matchDateIndex-1]/resistLinePoint<=1.01:
                if curStock.dayPriceClosedFList[matchDateIndex-1]<=resistLinePoint:
                    resultLine+=u"\t注意压力位！"
                if curStock.dayPriceClosedFList[matchDateIndex-1]>=resistLinePoint:
                    resultLine+=u"\t支撑位！"
            print resultLine


    ## 市场情绪
    volumeEnerge.moodIndexMarket(curStock.stockID,showDateInterval=90)
    
## 3.仓位控制和仓位止损控制
##长线止损
##中线止损
##短线止损

##  止损位设计

if __name__ == "__main__":
 
    startClock=time.clock() ##记录程序开始计算时间
    Ccomfunc.printInfor()
#    calGDG()
    
    stockIDList=configOS.stockIDMarketList
    for stockID in ["999999"]:
        main(stockID)
    
    timeSpan=time.clock()-startClock

    print("Time used(s):",round(timeSpan,2))
