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

def mainAppCall(strDate=""):
    stockID = "300468"
    stockPatternRecognitionMarket.recogitionPattern(stockID,strDate) 



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
    mainAppCall(strDate)
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


