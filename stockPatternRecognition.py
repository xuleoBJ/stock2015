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
    
    lineWritedList.append(u"日期    \t星期\t次日涨幅\t次日开盘\t量能\t")
    for index in kMatchIndexList: 
        resultLine= u"{0:<10}\t{1}\t{2}\t{3}\t{4}\t".format(curStock.dayStrList[index],curStock.weekDayList[index],\
                        curStock.dayRiseRateCloseFList[index+1],curStock.dayRiseRateOpenFList[index+1], \
                        curStock.dayRadioLinkOfTradeVolumeFList[index]\
                       )
        lineWritedList.append(resultLine)
##趋势日涨幅
#        resultLine=u"------趋势涨幅(日):"
#        for intervalDay in [-20,-10,-5,3,5,8,13]:
#            resultLine+=u" ({}){:.1f}".format(intervalDay,trendAna.calRiseRateInterval(curStock,index,intervalDay))
#        lineWritedList.append(resultLine)

##利用个股和对应大盘的同步性分析 进行模式识别
## matchDateIndex是要识别的strDate在序列中的指数位置 -1 是最新一个交易日
def patternRecByMarketAndStock(curMarket,curStock,matchDateIndex):
    ##根据涨幅进行历史K线模式识别,iTradeDay curStock周期，kNum是K线组合个数
    ##需要增加从某一天开始的模式
    kMatchIndexList=[] ##匹配的模式个数
    print ("-"*8+u"根据大盘和个股的2日涨幅进行条件匹配模式识别，500个交易日之内：")
    for i in range(-500,-1):
	    bSelect=True
	    iCount=0
	    bias=0.5
	    indexMarket=curMarket.dayStrList.index(curStock.dayStrList[i])
	    while iCount<=2 and bSelect==True:
		    ## 考虑大盘
		    valueRate=math.floor(curMarket.dayRiseRateCloseFList[matchDateIndex-iCount]/bias)*bias
		    if not valueRate<=curMarket.dayRiseRateCloseFList[indexMarket-iCount]<=valueRate+bias:
			    bSelect=False
		    iCount=iCount+1
	    bias=0.5
	    iCount=0
	    while iCount<=2 and bSelect==True:
		    ## 考虑个股
		    valueRate=math.floor(curStock.dayRiseRateCloseFList[matchDateIndex-iCount]/bias)*bias
		    if not valueRate<=curStock.dayRiseRateCloseFList[i-iCount]<=valueRate+bias:
			    bSelect=False
		    iCount=iCount+1
	    if bSelect==True:
		    kMatchIndexList.append(i)
    print kMatchIndexList 
    return kMatchIndexList

def patternRecByRiseRate(curStock,iTradeDay,kNum,matchDateIndex,bias=0.3):
    ##根据涨幅进行历史K线模式识别,iTradeDay curStock周期，kNum是K线组合个数
    ##需要增加从某一天开始的模式
    kMatchIndexList=[] ##匹配的模式个数
    print ("-"*8+u"根据前{}涨幅,自动设置条件,模式识别：".format(kNum))
    for i in range(-iTradeDay+kNum,-1):
	    iCount=0
	    bSelect=True
	    while iCount<=kNum-1 and bSelect==True:
		    ## 考虑涨幅
		    valueRate=math.floor(curStock.dayRiseRateCloseFList[matchDateIndex-iCount]/bias)*bias
		    if not valueRate<=curStock.dayRiseRateCloseFList[i-iCount]<=valueRate+bias:
			    bSelect=False
		    iCount=iCount+1
	    if bSelect==True:
		    kMatchIndexList.append(i)
    return kMatchIndexList

## 在利用K线组合的匹配的结果中，用开盘价进行过滤 
def patternRecByPriceOpen(curStock,matchDateIndex,kMatchIndexList,bias=0.3):
    ##根据前几日涨幅及开盘价进行历史K线模式识别：
    selectFromKmatchList=[]
    for index in kMatchIndexList:
	    iCount=0
	    valueRate=math.floor(curStock.dayPriceOpenFList[matchDateIndex-iCount]/bias)*bias
	    if  valueRate-bias<=curStock.dayPriceOpenFList[index-iCount]<=valueRate+bias: 
		     selectFromKmatchList.append(index)
    printResult(curStock,selectFromKmatchList)


## 在利用K线组合的匹配的结果中，用波动幅度进行过滤 
def patternRecByRiseWave(curStock,matchDateIndex,kMatchIndexList,bias=0.5):
    selectFromKmatchList=[]
    for index in kMatchIndexList:
	    iCount=0
	    valueRate=math.floor(curStock.dayWaveRateFList[matchDateIndex-iCount]/bias)*bias
#	    print valueRate
	    if  valueRate-bias<=curStock.dayWaveRateFList[index-iCount]<=valueRate+bias: 
		     selectFromKmatchList.append(index)
    printResult(curStock,selectFromKmatchList)

def patterRecByVolume(curStock,matchDateIndex,kMatchIndexList,kNum):
    selectFromKmatchList=[]
    for index in kMatchIndexList:
	    iCount=0
    ##成交量要同步增加或者减少,条件是考虑成交量筛选，成交量量比同时大于1 同真或者同假
	    bSyn=True
	    while iCount<kNum:
		        if  (curStock.dayRadioLinkOfTradeVolumeFList[index-iCount]>=1) != (curStock.dayRadioLinkOfTradeVolumeFList[matchDateIndex-iCount]>=1):
			            bSyn=False
		        iCount=iCount+1
	    if bSyn==True:
		        selectFromKmatchList.append(index)
    printResult(curStock,selectFromKmatchList)

def patterRecByHandSet(curStock,iTradeDay,kNum):
    ## 手动设置查找条件
    print ("-"*8+u"手动设置条件查找历史K线：")
    riseRate_i=int(curStock.dayRiseRateCloseFList[-1])
    riseRate_i_1=int(curStock.dayRiseRateCloseFList[-2])
    for i in range(-iTradeDay+2,-1):
        bSelect=False
        ##自动设置条件，用最后两个交易日做基准
        if  riseRate_i_1<=curStock.dayRiseRateCloseFList[i-1]<=1+riseRate_i_1 and riseRate_i<=curStock.dayRiseRateCloseFList[i]<=1+riseRate_i:
        ##手工设置if条件
#        if  curStock.dayRiseRateCloseFList[i-1]<=0 and 5<=curStock.dayRiseRateCloseFList[i]<=7:
            bSelect=True
        if  bSelect==True:
            weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday() 
            print(curStock.dayStrList[i],"weekDay_"+str(weekDay),"RiseRateofNextTradeDay: "+str(curStock.dayRiseRateCloseFList[i+1]))
            print(u"{},星期{},次日涨幅:{}".format(curStock.dayStrList[i],weekDay,curStock.dayRiseRateCloseFList[i+1]))
            print("_"*30+"riseRate",curStock.dayRiseRateCloseFList[i-2],curStock.dayRiseRateCloseFList[i-1],curStock.dayRiseRateCloseFList[i])
            print("_"*30+"turnOverRate=",curStock.dayRiseOfTurnOverFList[i-2],curStock.dayRiseOfTurnOverFList[i-1],curStock.dayRiseOfTurnOverFList[i-1])

def addInforLine(inforLine):
    lineWritedList.append("-"*72)
    lineWritedList.append(inforLine)

    ## 默认的是最后一个交易日作匹配模型
def recogitionPattern(stockID,strDate=""):
    ##读取股票代码，存储在curStock里
    curStock=Cstock.Stock(stockID)
    
    matchDateIndex = Ccomfunc.getIndexByStrDate(curStock,strDate)

    lineWritedList.append("-"*72)
    lineWritedList.append(stockID)

    ##设置分析周期,缺省为1000，是4年的行情
    iTradeDay=1000
    if stockID=="999999":
        iTradeDay=len(curStock.dayStrList)
    ##起始分析日期 dateStrStart
    dateStrStart=curStock.dayStrList[-iTradeDay]
    ##终了分析日期 dateStrEnd
    dateStrEnd=curStock.dayStrList[-1]

    inforLine= "-"*8+u"正在查找历史K线日期：！！！！日期选完，请注意看K线趋势，同时注意成交量的表现："
    addInforLine(inforLine)
    
    kNum=3 ##需要分析的K线天数
    bias=0.5 ##涨幅取值范围，个股用1，大盘指数用0.5
    if stockID not in ["999999"] :
        bias=1.0
    
    inforLine="-"*8+u"最近交易日的相关数据："
    addInforLine(inforLine)
    
    lineWritedList.append("星期\t涨幅:\t 量比:\t波动幅度:")
    for i in range(matchDateIndex+1-kNum,matchDateIndex+1): ##循环指数起始比匹配指数少1
        weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday() 
        resultLine=u"{}\t{}\t{}\t{}".format(curStock.dayStrList[i],weekDay,curStock.dayRiseRateCloseFList[i],\
                curStock.dayRadioLinkOfTradeVolumeFList[i],curStock.dayWaveRateFList[i])
        lineWritedList.append(resultLine)
    
    print("-"*72)
    kPatternList=patternRecByRiseRate(curStock,iTradeDay,kNum,matchDateIndex,bias)
    printResult(curStock,kPatternList)
    
   ## inforLine=u"增加开盘价涨幅匹配条件："
   ## addInforLine(inforLine)
   ## patternRecByPriceOpen(curStock,matchDateIndex,kPatternList)
    
   ## inforLine=u"增加振幅匹配条件："
   ## addInforLine(inforLine)
   ## patternRecByRiseWave(curStock,matchDateIndex,kPatternList)
    
    inforLine=u"增加成交量匹配条件："
    addInforLine(inforLine)
    patterRecByVolume(curStock,matchDateIndex,kPatternList,kNum)
	
dirPatternRec = "patternRecDir"

def mainAppCall(strDate=""):
    del configOS.patternRecDateListSH[:]
    del configOS.patternRecDateListSZ[:]
    del configOS.patternRecDateListCYB[:]

    for stockID in configOS.stockIDMarketList: 
        recogitionPattern(stockID,strDate) ##-1是最后一个交易日分析

    configOS.updatePetternRectDateList()

    for line in lineWritedList:
        print line
    
    now = datetime.datetime.now()
    endTime = now.replace(hour=15, minute=00, second=0, microsecond=0)
    if now <= endTime:
        dayStr=datetime.date.today().strftime("%Y%m%d")
    else:
        dayStr=(datetime.date.today()+datetime.timedelta(days=1)).strftime("%Y%m%d")
    goalFilePath= os.path.join( dirPatternRec, dayStr+".txt" ) ##输出文件名
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    os.startfile(goalFilePath)

if __name__=="__main__":
    
    ##模式识别的方法，如果最近3天的没有 可以用前三天的往后推
    startClock=time.clock() ##记录程序开始计算时间
    mainAppCall()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


