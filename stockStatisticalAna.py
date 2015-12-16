# -*- coding: utf-8 -*- 
import os
import shutil
import time
import datetime
import math
import Cstock
import sys
import Ccomfunc,trendAna
import configOS
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter  

import numpy as np
import matplotlib.mlab as mlab

lineWritedList=[]

def printResult(curStock,kMatchIndexList):
    ##识别结果统计分析
    dateList=[]
 
    lineWritedList.append(u"识别结果：{},涨幅> ".format(len(dateList)))
    dateStrLine='\t'.join(dateList)
    lineWritedList.append(dateStrLine)
    
    headLine=u"日期\t星期\t前日涨幅\t量幅\t当日涨幅:\t前3日涨幅\t前5日涨幅"
    lineWritedList.append(headLine)
    dataX=[]
    for index in kMatchIndexList: 
        weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[index]).isoweekday()
        riseRate3B=trendAna.calRiseRateInterval(curStock,index,-3)
        riseRate5B=trendAna.calRiseRateInterval(curStock,index,-5)
        dataX.append(curStock.dayRiseRateFList[index-1])
        resultLine= u"{}\t星期{}\t{}\t{}\t{}\t{:.2f}\t{:.2f}".format(curStock.dayStrList[index],weekDay,\
                        curStock.dayRiseRateFList[index-1],curStock.dayRadioLinkOfTradeVolumeFList[index-1],curStock.dayRiseRateFList[index],\
                        riseRate3B,riseRate5B)
        lineWritedList.append(resultLine)

    ##输出到文件
    for line in lineWritedList:
        print line
    goalFilePath="ResultStatictics.txt" ##输出文件名
    Ccomfunc.write2Text(goalFilePath,lineWritedList) 
    ##绘图分析
    if len(dataX)>0:
        num_bins = 10
        # the histogram of the data
        n, bins, patches = plt.hist(dataX, num_bins, normed=1, facecolor='green', alpha=0.5)
        # add a 'best fit' line
        mu = 100  # mean of distribution
        sigma = 15  # standard deviation of distribution
        y = mlab.normpdf(bins, mu, sigma)
        plt.plot(bins, y, 'r--')
        plt.xlabel('Smarts')
        plt.ylabel('%')
        plt.title(r'Histogram of result: ')

        plt.subplots_adjust(left=0.15)
        plt.show()

def addInforLine(inforLine):
    lineWritedList.append("-"*72)
    lineWritedList.append(inforLine)

def main(stockID,strDate=""):
    curStock=Cstock.Stock(stockID)
    curStock.list2array()
    
    curMarketStock=Ccomfunc.getMarketStock(stockID)
    
    lineWrited=[]
    headline="日期\tcur开盘\tcur收盘\tcur最低\tcur最高\tcur最低\tmarket最低\tcur最高\tmarket最高\tcur波动幅度\tmarket波动幅度"
    lineWrited.append( headline )
    for i in range(-60,0):
        j=curMarketStock.dayStrList.index( curStock.dayStrList[i] ) ## curStock 和 curMarketStock 不一定是相同指数，由于停牌等等原因
        wordList=[]
        wordList.append( str( curStock.dayStrList[i] ) )
        wordList.append( str( curStock.dayPriceOpenArray[i] ) )
        wordList.append( str( curStock.dayPriceLowestArray[i] ) )
        wordList.append( str( curStock.dayPriceHighestArray[i] ) )
        wordList.append( str( curStock.dayPriceClosedFList[i] ) )
        wordList.append( str( curStock.dayRiseRateLowestArray[i] ) )
        wordList.append( str( curMarketStock.dayRiseRateLowestArray[j] ) ) 
        wordList.append( str( curStock.dayRiseRateHighestArray[i] ) )
        wordList.append( str( curMarketStock.dayRiseRateHighestArray[j] ) )
        wordList.append( str( curStock.dayWaveRateArray[i] ) )
        wordList.append( str( curMarketStock.dayWaveRateArray[j] ) )
        lineWrited.append("\t".join(wordList))
    
    goalFilePath="ana.txt"
    Ccomfunc.write2Text(goalFilePath,lineWrited)
    indexDateStart=0
    indexDateEnd=len(curStock.dayStrList)
    
    ##手工设置条件，前日最低，前日最高，前日波动，今日开盘价，然后统计分析
    print("-"*72)
    kPatternList=[]
    for i in range(indexDateStart,indexDateEnd):
        if curStock.dayOpenRateArray[i]<=-0.9 and -0.7<=curStock.dayPriceClosedArray[i-1]<=-0.5:
            kPatternList.append(i)
    printResult(curStock,kPatternList)
    

def mainAppCall(strDate=""):
    main("002152") ##-1是最后一个交易日分析


if __name__=="__main__":
    
    ##模式识别的方法，如果最近3天的没有 可以用前三天的往后推
    startClock=time.clock() ##记录程序开始计算时间
    mainAppCall()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


