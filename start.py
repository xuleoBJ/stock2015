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



def main(curStock):
    ## 读取配置文件，获取相关信息，活得股票ID,实例化 curStock
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
     
    print(u"-"*72)
    print(u"当前市场定义：强势，弱势？上升市，下跌市，震荡市？这个月的目标是啥？")
    print(u"-"*72)

    ## 1. 首先要做趋势分析！趋势分为长期，中期，短期趋势
    print(u"1-时空趋势分析")
    print (u"-"*72)
    print (u"正在进行时间趋势分析：")
   
    for period in [10,20,30,60,120]:
        indexHighPoint=curStock.dayPriceHighestFList.index(max(curStock.dayPriceHighestFList[-period:]))
        riseHighcurrent=100*(curStock.dayPriceClosedFList[-1]-curStock.dayPriceHighestFList[indexHighPoint])/curStock.dayPriceHighestFList[indexHighPoint]
        rateHighTradeVolumecurrent=curStock.dayTradeVolumeFList[-1]/curStock.dayTradeVolumeFList[indexHighPoint]
        indexLowPoint=curStock.dayPriceLowestFList.index(min(curStock.dayPriceLowestFList[-period:]))
        riseLowcurrent=100*(curStock.dayPriceClosedFList[-1]-curStock.dayPriceLowestFList[indexLowPoint])/curStock.dayPriceLowestFList[indexLowPoint]
        rateLowTradeVolumecurrent=curStock.dayTradeVolumeFList[-1]/curStock.dayTradeVolumeFList[indexLowPoint]
        print(u"{}日高点{}，日期{}，距今{}个交易日,涨幅{:.2f}%，量能比{:.2f}".format(period,curStock.dayPriceHighestFList[indexHighPoint], \
                curStock.dayStrList[indexHighPoint],len(curStock.dayStrList)-1-indexHighPoint,riseHighcurrent,rateHighTradeVolumecurrent))
        print(u"{}日低点{}，日期{}，距今{}个交易日,涨幅{:.2f}%，量能比{:.2f}".format(period,curStock.dayPriceLowestFList[indexLowPoint], \
                curStock.dayStrList[indexLowPoint],len(curStock.dayStrList)-1-indexLowPoint,riseLowcurrent,rateLowTradeVolumecurrent))

    ## 时空分析,关键支撑分析
    print(u"-"*72)
    print(u"关键点位提示分析：")
    print(u"-"*72)
    for period in [20,60,120,180]:
        cycleHigh=curStock.dayPriceHighestArray[-period:].max()
        cycleLow=curStock.dayPriceLowestArray[-period:].min()
        for keyPoint in [0.33,0.5,0.825]:
            resistLinePoint=cycleLow+(cycleHigh-cycleLow)*keyPoint
            print(u"{}日 低点:{}，高点:{}，{}线:{:.2f}".format(period,cycleLow,cycleHigh,keyPoint,resistLinePoint))
            if(abs(curStock.dayPriceClosedFList[-1]-resistLinePoint)<=50):
                print(u"注意压力位！")

    print(u"-"*72)
    print(u"2-当月趋势分析")
    ##  分析当月涨幅
    riseCurrentMonth=trendAna.calRiseRateCurrentMonth1st2today(curStock)
    print(u"月初到今日涨幅：{:.2f}".format(riseCurrentMonth))
    ##  分析近年同期走势
    print(u"-"*72)
    numOfyear=10
    trendAna.trendOfMonthHistory(curStock,numOfyear)

    print(u"-"*72)
    print(u"3-市场情绪趋势分析")
    volumeEnerge.moodIndex(curStock,200)

    
## 3.仓位控制和仓位止损控制
##长线止损
##中线止损
##短线止损

##  止损位设计

if __name__ == "__main__":
 
    startClock=time.clock() ##记录程序开始计算时间
    Ccomfunc.printInfor()
    print(u"当前市场定义：强势，弱势？上升市，下跌市，震荡市？这个月的目标是啥？")
#    calGDG()
    
    stockIDList=configOS.stockIDMarketList
    for stockID in ["999999"]:
        curStock=Cstock.Stock(stockID)
        curStock.list2array()
        main(curStock)
#    
#    for stockID in configOS.stockIDList:
#        curStock=Cstock.Stock(stockID)
#        curStock.list2array()
#        stockTecSet.main(curStock)
    
    timeSpan=time.clock()-startClock

    print("Time used(s):",round(timeSpan,2))
