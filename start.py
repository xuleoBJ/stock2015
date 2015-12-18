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

def main(stockID):
    curStock=Cstock.Stock(stockID)
    curStock.list2array()
    ## 读取配置文件，获取相关信息，活得股票ID,实例化 curStock
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    
    today=datetime.date.today()
    print(u"-"*72)
    print(u"近期市场分析：")
    for i in range(-5,0):
        weekDay=curStock.dateList[i].isoweekday() 
        print(u"{}:星期{} 涨幅{:.2f}%\t量能比{:.2f}".format(curStock.dayStrList[i], weekDay ,curStock.dayRiseRateFList[i],\
                curStock.dayRadioLinkOfTradeVolumeFList[i]))
     
    print(u"-"*72)

    ## 1. 首先要做趋势分析！趋势分为长期，中期，短期趋势
    print(u"1-时空趋势分析")
    print (u"-"*72)
    print (u"正在进行时间趋势分析：")
    
    headline=u"周期(日) 高(低)点\t日期\t交易日数\t涨幅%\t量能比"
    print (headline)
    for period in [10,20,30,60,120]:
        indexHighPoint=-period+curStock.dayPriceHighestArray[-period:].argmax()
        riseHighcurrent=100*(curStock.dayPriceClosedFList[-1]-curStock.dayPriceHighestFList[indexHighPoint])/curStock.dayPriceHighestFList[indexHighPoint]
        rateHighTradeVolumecurrent=curStock.dayTradeVolumeFList[-1]/curStock.dayTradeVolumeFList[indexHighPoint]
        indexLowPoint=-period+curStock.dayPriceLowestArray[-period:].argmin()
        riseLowcurrent=100*(curStock.dayPriceClosedFList[-1]-curStock.dayPriceLowestFList[indexLowPoint])/curStock.dayPriceLowestFList[indexLowPoint]
        rateLowTradeVolumecurrent=curStock.dayTradeVolumeFList[-1]/curStock.dayTradeVolumeFList[indexLowPoint]
        print(u"{}日\t{}\t{}\t{}\t{:.2f}\t{:.2f}".format(period,curStock.dayPriceHighestFList[indexHighPoint], \
                curStock.dayStrList[indexHighPoint],-indexHighPoint,riseHighcurrent,rateHighTradeVolumecurrent))
        print(u"{}日\t{}\t{}\t{}\t{:.2f}\t{:.2f}".format(period,curStock.dayPriceLowestFList[indexLowPoint], \
                curStock.dayStrList[indexLowPoint],-indexLowPoint,riseLowcurrent,rateLowTradeVolumecurrent))

    ## 时空分析,关键支撑分析
    print(u"-"*72)
    print(u"关键点位提示分析：")
    print(u"-"*72)
    headline=u"周期(日)幅度\t低点\t高点\t点位"
    print (headline)
    for period in [20,60,120,180]:
        cycleHigh=curStock.dayPriceHighestArray[-period:].max()
        cycleLow=curStock.dayPriceLowestArray[-period:].min()
        for keyPoint in [0.33,0.5,0.825]:
            resistLinePoint=cycleLow+(cycleHigh-cycleLow)*keyPoint
            resultLine=u"{}\t{}\t{}\t{}\t{:.2f}".format(period,keyPoint,cycleLow,cycleHigh,resistLinePoint)
            if 0.99<=curStock.dayPriceClosedFList[-1]/resistLinePoint<=1.01:
                if curStock.dayPriceClosedFList[-1]<=resistLinePoint:
                    resultLine+=u"\t注意压力位！"
                if curStock.dayPriceClosedFList[-1]>=resistLinePoint:
                    resultLine+=u"\t支撑位！"
            print resultLine

    print(u"-"*72)
    print(u"3-市场情绪趋势分析")
    volumeEnerge.moodIndex(stockID)

    
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
