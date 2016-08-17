# -*- coding: utf-8 -*- 
import os
import shutil
import time
import datetime
import math
import Cstock
import sys
import Ccomfunc
import stockTrendAna
import configOS
import stockPatternRecognitionMarket
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter  

lineWritedList=[]

def recogitionPatternByDateStr(curStock,strDate):
    matchDateIndex = Ccomfunc.getIndexByStrDate(curStock,strDate)
    recogitionPatternByDateIndex(curStock,matchDateIndex)
    
    ## 默认的是最后一个交易日作匹配模型
def recogitionPatternByDateIndex(curStock,matchDateIndex):
    ##读取股票代码，存储在curStock里

    lineWritedList.append("-"*72)
    lineWritedList.append(curStock.stockID)

    ##设置分析周期,缺省为1000，是4年的行情
    iTradeDay=1000
    if curStock.stockID in ["999999","399001"]:
        iTradeDay=len(curStock.dayStrList)
    ##起始分析日期 dateStrStart
    dateStrStart=curStock.dayStrList[-iTradeDay]
    ##终了分析日期 dateStrEnd
    dateStrEnd=curStock.dayStrList[-1]

    inforLine= "-"*8+u"正在查找历史K线日期：！！！！日期选完，请注意看K线趋势，同时注意成交量的表现："
    stockPatternRecognitionMarket.addInforLine(inforLine)
    
    kNum=3 ##需要分析的K线天数
    bias=0.5 ##涨幅取值范围，个股用1，大盘指数用0.5
    if curStock.stockID not in ["999999"] :
        bias=1.0
    
    inforLine="-"*8+u"最近交易日的相关数据："
    stockPatternRecognitionMarket.addInforLine(inforLine)
    
    lineWritedList.append("日期[星期]    \t涨幅\t最大涨幅\t最小涨幅\t量比\t波动幅度\t")
    for i in range(matchDateIndex+1-kNum,matchDateIndex+1): ##循环指数起始比匹配指数少1
        weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday() 
        resultLine=u"{}[{}]\t{}\t{}\t{}\t{}\t{}".format(curStock.dayStrList[i],weekDay,curStock.dayRiseRateCloseFList[i], curStock.dayRiseRateHighestArray[i], curStock.dayRiseRateLowestFList[i], \
                curStock.dayRadioLinkOfTradeVolumeFList[i],curStock.dayWaveRateFList[i])
        lineWritedList.append(resultLine)
    
    print("-"*72)
    kPatternList=patternRecByRiseRate(curStock,iTradeDay,kNum,matchDateIndex,bias)
    printResult(curStock,kPatternList)
    

    print("-"*72)
    print(u"计算市场情绪指数")
    moodIndex = calMoodIndexFromRecogitionPattern(curStock,iTradeDay,kNum,matchDateIndex,bias)
    print (u"昨日市场情绪指数{:.2f}".format(moodIndex)) 
   ## inforLine=u"增加开盘价涨幅匹配条件："
   ## addInforLine(inforLine)
   ## patternRecByPriceOpen(curStock,matchDateIndex,kPatternList)
    
   ## inforLine=u"增加振幅匹配条件："
   ## addInforLine(inforLine)
   ## patternRecByRiseWave(curStock,matchDateIndex,kPatternList)
    
    inforLine=u"增加成交量匹配条件："
    stockPatternRecognitionMarket.addInforLine(inforLine)
    patterRecByVolume(curStock,matchDateIndex,kPatternList,kNum)

def printResult(curStock,kMatchIndexList):
    ##识别结果统计分析
    dateList=[]
    riseRateNextList=[]
    riseRateHighestNextList=[]
    riseRateLowestNextList=[]
    for i in kMatchIndexList:
        dateList.append(curStock.dayStrList[i])
        riseRateNextList.append(curStock.dayRiseRateCloseFList[i+1])
        riseRateHighestNextList.append(curStock.dayRiseRateHighestFList[i+1])
        riseRateLowestNextList.append(curStock.dayRiseRateLowestFList[i+1])
        if curStock.stockID=="999999" and (not curStock.dayStrList[i] in configOS.patternRecDateListSH) :
            configOS.patternRecDateListSH.append(curStock.dayStrList[i])
        if curStock.stockID=="399001" and (not curStock.dayStrList[i] in configOS.patternRecDateListSZ) :
            configOS.patternRecDateListSZ.append(curStock.dayStrList[i])
    
    matchNum=len(kMatchIndexList)
    value0_smaller0=len(filter(lambda x:x<=0,riseRateNextList))
    value_smaller_1=len(filter(lambda x:x<=-1,riseRateNextList))
    value_bigger1=len(filter(lambda x:x>=1,riseRateNextList))
    if matchNum>0:
        lineWritedList.append("-"*72)
        lineWritedList.append(u"模式识别结果统计:")
        lineWritedList.append(u"统计总数\t<=0(占比%)\t>=1\t<-1")
        lineWritedList.append(u"{:2d}   \t{:2d}({:.2f}%)\t{}\t{}".format( \
                matchNum,value0_smaller0,float(value0_smaller0)*100/matchNum,value_bigger1,value_smaller_1))
        valueLine='\t'.join(map(str,sorted(riseRateNextList)))
        _median=np.median(riseRateNextList)
        lineWritedList.append(u"收盘涨幅:{}".format(valueLine))
        lineWritedList.append(u"收盘涨幅中位数:{:.2f}".format(_median))
#        valueHighestLine='\t'.join(map(str,sorted(riseRateHighestNextList)))
#        _median=np.median(riseRateHighestNextList)
#        lineWritedList.append(u"最高涨幅:{}\t中位数:{:.2f}".format(valueHighestLine,_median))
#        valueLowestLine='\t'.join(map(str,sorted(riseRateLowestNextList)))
#        _median=np.median(riseRateLowestNextList)
#        lineWritedList.append(u"最低涨幅:{}\t中位数:{:.2f}".format(valueLowestLine,_median))
    lineWritedList.append("-"*72)
    
    lineWritedList.append(u"日期[星期]\t次日涨幅\t次日开盘\t次日最高\t次日最低\t量能\t当日涨幅")
    for index in kMatchIndexList: 
        resultLine= u"{0:<10}[{1}]\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}".format(curStock.dayStrList[index],curStock.weekDayList[index],\
                        curStock.dayRiseRateCloseFList[index+1],curStock.dayRiseRateOpenFList[index+1],\
                        curStock.dayRiseRateHighestArray[index+1],curStock.dayRiseRateLowestArray[index+1],\
                        curStock.dayRadioLinkOfTradeVolumeFList[index],curStock.dayRiseRateCloseArray[index]\
                       )
        lineWritedList.append(resultLine)
dirPatternRec = "patternRecDir"



if __name__=="__main__":
    
    ##模式识别的方法，如果最近3天的没有 可以用前三天的往后推
    startClock=time.clock() ##记录程序开始计算时间
    
    strDate=""

    now = datetime.datetime.now()
    marketStartTime = now.replace(hour=9, minute=30, second=0, microsecond=0)
    marketEndTime = now.replace(hour=15, minute=00, second=0, microsecond=0)
    
    ##根据时间自动取strDate,开盘之前 以后取昨天，下午三点以前今天
    if strDate=="" and now <= marketEndTime:
        strDate=(datetime.date.today()-datetime.timedelta(days=1)).strftime("%Y/%m/%d")
    if strDate=="" and now >= marketEndTime:
        strDate=datetime.date.today().strftime("%Y/%m/%d")

    stockID = "600707"
    curStock=Cstock.Stock(stockID)
    recogitionPatternByDateStr(curStock,strDate) 
     
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


