# -*- coding: utf-8 -*-
import os
import datetime,time
#import ConfigParser
import Cstock
import Ccomfunc
# import configOS
import stockPatternRecognition
import stockTradeModel
# import stockTrendAna
import ctypes 

from PyQt4 import QtGui # Import the PyQt4 module we'll need
from PyQt4.QtGui import *

lineWritedList=[]

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
    ctypes.windll.user32.MessageBoxA(0, "goal:3200,sell:1/2", "infor", 1)

##历史上相同的周，和相同的交易日
def specialWeekDaySatis(curStock,strDate):
    print (strDate)

##历史上的今天
def specialDateSatis(curStock,strDate):
    print (strDate)
    resultLine= u"代码\t日期\t当日涨幅\t次日涨幅\t前日涨幅"
    print (resultLine)
    split = strDate.split('/')
    for iYear in range(2000,2016):
        inputStr="/".join([str(iYear),split[1],split[2]])
        index=Ccomfunc.getIndexByStrDate(curStock,inputStr)+1
        resultLine= u"{}\t{}({})\t{}\t{}\t{}".format( \
                curStock.stockID,curStock.dayStrList[index], curStock.weekDayList[index], \
                curStock.dayRiseRateCloseFList[index],curStock.dayRiseRateCloseFList[index+1],curStock.dayRiseRateCloseFList[index-1])
        print (resultLine)

def main(stockID,strDate=Ccomfunc.defaultDateInputStr()):
    ##近期事务提醒，希望建立数据库
    WarnBigEvent() 
    curStock=Cstock.Stock(stockID)
   
    matchDateIndex = Ccomfunc.getIndexByStrDate(curStock,strDate)
    print (u"分析日期：{}".format(curStock.dayStrList[matchDateIndex]))

    print(u"-"*72)
    print(u"近期市场分析：")
    headLine=u"日期[星期]\t涨幅\t最高\t最低\t量能\t描述"
    print(headLine)
    for i in range(matchDateIndex-5,matchDateIndex+1):
        weekDay = curStock.dateList[i].isoweekday()
        marketSummaryStr = stockTrendAna.marketSummary(curStock,i)
        print(u"{}[{}]\t{:.2f}%\t{:.2f}%\t{:.2f}%\t{}\t{}".format(curStock.dayStrList[i], weekDay , \
                curStock.dayRiseRateCloseFList[i],\
                curStock.dayRiseRateHighestArray[i],\
                curStock.dayRiseRateLowestArray[i],\
                curStock.dayRadioLinkOfTradeVolumeFList[i], marketSummaryStr))
    
    ## 通过大盘上证成交量判断目前的市场位置,30日均线的位置
    if curStock.stockID == "999999":
        if curStock.dayTurnOverArray[matchDateIndex]>=2000*10**8:
            print (u"市场强势")
        elif 1500*10**8<=curStock.dayTurnOverArray[matchDateIndex]<2000*10**8:
            print (u"平衡市场")
        elif curStock.dayTurnOverArray[matchDateIndex]<=1500*10**8:
            print (u"弱市场")
        if curStock.dayPriceClosedArray[matchDateIndex] < curStock.day30PriceAverageArray[matchDateIndex] :
            print (u"30日均线以下")
        else:
            print (u"30日均线以上")
        if curStock.dayPriceClosedArray[matchDateIndex] < curStock.day5PriceAverageArray[matchDateIndex] :
            print (u"5日均线以下")
        else:
            print (u"5日均线以上")
    ## 历史上的今天
    print (u"-"*72)
    headLine=u"历史上今天的涨幅:"
    print(headLine)
    specialDateSatis(curStock,strDate)
   
   
    ## 近期跳水、爬升统计分析,已7天作为一个周期：
    ## 1. 首先要做趋势分析！趋势分为长期，中期，短期趋势
    ## 近期跳水、爬升统计分析,已7天作为一个周期：
    print(u"-"*72)
    ##stockTrendAna.UpDownStasticFor(curStock,matchDateIndex,10)
    ##print(u"-"*72)
    
    ## 均价分析
    print (u"-"*72)
    print (u"均价分析：")
    headLine=u"\t3日\t5日\t10日\t30日"
    print(headLine)
    print(u"价 {}\t{}\t{}\t{}".format(curStock.day3PriceAverageArray[matchDateIndex],curStock.day5PriceAverageArray[matchDateIndex],\
            curStock.day10PriceAverageArray[matchDateIndex],curStock.day30PriceAverageArray[matchDateIndex]) )
##    print(u"量 {}\t{}\t{}\t{}".format(curStock.day3TradeVolumeArray[matchDateIndex],curStock.day5TradeVolumeArray[matchDateIndex],\
##            curStock.day10TradeVolumeArray[matchDateIndex],curStock.day20TradeVolumeArray[matchDateIndex]) )
    print (u"-"*72)
    
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
    for period in [5,10,20,30,60,90,120,150,180]:
        cycleHigh=curStock.dayPriceHighestArray[matchDateIndex-period:matchDateIndex+1].max()
        cycleLow=curStock.dayPriceLowestArray[matchDateIndex-period:matchDateIndex+1].min()
        for keyPoint in [0.25,0.33,0.5,0.618,0.825]:
            resistLinePoint=cycleLow+(cycleHigh-cycleLow)*keyPoint
            calRiseRate = -999
            if resistLinePoint != 0:
                calRiseRate = 100*(resistLinePoint-curStock.dayPriceClosedArray[-1])/resistLinePoint
            resultLine=u"{}日\t{}\t{}\t{}\t{:.2f}\t{:.2f}%".format(period,keyPoint,cycleLow,cycleHigh,resistLinePoint,calRiseRate)
            if 0.99<=curStock.dayPriceClosedFList[matchDateIndex]/resistLinePoint<=1.01:
                if curStock.dayPriceClosedFList[matchDateIndex]<=resistLinePoint:
                    resultLine+=u"\t注意压力位！"
                if curStock.dayPriceClosedFList[matchDateIndex]>=resistLinePoint:
                    resultLine+=u"\t支撑位！"
            print (resultLine)



def mainAppCall(strDate=""):
    for line in lineWritedList:
        print (line)
    
    dayStr=strDate.replace("/","")
    goalFilePath= os.path.join( dirPatternRec, dayStr+".txt" ) ##输出文件名
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    os.startfile(goalFilePath)

if __name__ == "__main__":
 
    startClock=time.clock() ##记录程序开始计算时间
    Ccomfunc.printInfor()
#    calGDG()
    
    stockIDList=configOS.stockIDMarketList
    for stockID in ["999999"]:
        main(stockID)
    
    timeSpan=time.clock()-startClock

    print("Time used(s):",round(timeSpan,2))
