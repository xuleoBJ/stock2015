# -*- coding: utf-8 -*- 
import os
import shutil
import subprocess
import time
import datetime
import math
import Cstock
import Ccomfunc
import getStockIDList
import sys
import configOS
import numpy as np


lineWritedList=[]


def addInforLine(inforLine):
    lineWritedList.append("-"*72)
    lineWritedList.append(inforLine)

def main(stockID,strDate=Ccomfunc.defaultDateInputStr()):
    print strDate
    curStock=Cstock.Stock(stockID)
    curMarketStock=Ccomfunc.getMarketStock(stockID)
    indexDate=Ccomfunc.getIndexByStrDate(curMarketStock,strDate)
    print indexDate

    lineWrited=[]
    headline="日期\tcur开盘\tcur收盘\tcur最低\tcur最高\tcur最低\tmarket最低\tcur最高\tmarket最高\tcur波动幅度\tmarket波动幅度"
    lineWrited.append( headline )

    for i in range(indexDate-60,indexDate):
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
    
    ##美股跌1.5以上

    ##大盘高开0.5点以上统计

    ##手工设置条件，前日最低，前日最高，前日波动，今日开盘价，然后统计分析
    print("-"*72)
    kPatternList=[]
    for i in range(indexDateStart,indexDateEnd):
        if curStock.dayOpenRateArray[i]>=0.5 and -999<=curStock.dayPriceClosedArray[i-1]<=-999:
            kPatternList.append(i)
    printResult(curStock,kPatternList)
    

##read stock, if openPrice - 0.5 , get riseRate
def openPriceSatis(stockID):
    lineWritedList=[]
    curStock=Cstock.Stock(stockID)
    headWordList=[]
    headWordList.append(u"日期    ")
    headWordList.append(u"星期")
    headWordList.append(u"开盘涨幅")
    headWordList.append(u"收盘涨幅")
    headWordList.append(u"T+1涨幅")
    headWordList.append(u"T+2涨幅")
    headWordList.append(u"距离上次交易日间隔天数")
    headWordList.append(u"区间涨幅")
    headLine="\t".join(headWordList)
    lineWritedList.append(headLine)
    print headLine
    lastRecordDay=0
    for i in range(0,len(curStock.dayStrList)):
        ## 这里设置条件
        ## 条件1：前交易日 大于0 开盘低开1个点
        #if curStock.dayRiseRateOpenFList[i-1]>=0 and curStock.dayRiseRateOpenFList[i]<=-1:
        if curStock.dayRiseRateOpenFList[i-1]>=0 and curStock.dayRiseRateOpenFList[i]<=-1:
            wordList=[]
            wordList.append(curStock.dayStrList[i])
            weekDay = curStock.dateList[i].isoweekday()
            wordList.append(str(weekDay))
            wordList.append(str(curStock.dayRiseRateOpenFList[i]))
            wordList.append(str(curStock.dayRiseRateCloseFList[i]))
            wordList.append(str(curStock.dayRiseRateCloseFList[i+1]))
            wordList.append(str(curStock.dayRiseRateCloseFList[i+2]))
            wordList.append(str(i-lastRecordDay))
            riseRateInter=100*(curStock.dayPriceClosedArray[i]-curStock.dayPriceClosedArray[lastRecordDay])/curStock.dayPriceClosedArray[lastRecordDay]
            wordList.append(str(round(riseRateInter,2)))
            lastRecordDay=i
            resultLine= "\t".join(wordList)
            lineWritedList.append(resultLine)
            print resultLine
    goalFilePath='_result.txt'
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    subprocess.call(['notepad.exe',goalFilePath])
    

if __name__=="__main__":
    
    startClock=time.clock() ##记录程序开始计算时间
    stockIDList = getStockIDList.makeStockListFromIDtxt("stockIDPlateIndex.txt")
    ##读取板块指数代码，存到List中
    print stockIDList
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


