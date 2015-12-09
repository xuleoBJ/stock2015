# -*- coding: utf-8 -*- 
import os
import shutil
import time
import datetime
import math
import Cstock
import sys
import Ccomfunc
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
        riseRate3B=Ccomfunc.calRiseRateInterval(curStock,index,-3)
        riseRate5B=Ccomfunc.calRiseRateInterval(curStock,index,-5)
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
    
    indexDateStart=0
    indexDateEnd=len(curStock.dayStrList)
    
    print("-"*72)
    kPatternList=[]
    for i in range(indexDateStart,indexDateEnd):
        if curStock.dayOpenRateArray[i]<-0.5:
            kPatternList.append(i)
    printResult(curStock,kPatternList)
    

def mainAppCall(strDate=""):
#    del configOS.patternRecDateListSH[:]
#    del configOS.patternRecDateListSZ[:]
#    del configOS.patternRecDateListCYB[:]
#    for stockID in configOS.stockIDMarketList: 
    riseRateOpen=-0.5
    main("999999",riseRateOpen) ##-1是最后一个交易日分析
    


if __name__=="__main__":
    
    ##模式识别的方法，如果最近3天的没有 可以用前三天的往后推
    startClock=time.clock() ##记录程序开始计算时间
    mainAppCall()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


