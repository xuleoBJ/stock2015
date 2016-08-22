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
    # print ("-"*8+u"根据前{}涨幅,自动设置条件,模式识别：".format(kNum))
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



def calMoodIndexTradeDay(curStock,dateIndex):
    pass


##计算昨日市场情绪指数
def calMoodIndexFromRecogitionPattern(curStock,iTradeDay,kNum,matchDateIndex,bias):
    kPatternListYestoday=patternRecByRiseRate(curStock,iTradeDay,kNum,matchDateIndex-1,bias)
    ##识别结果统计分析
    dateList=[]
    riseRateNextList=[]
    for i in kPatternListYestoday:
        dateList.append(curStock.dayStrList[i])
        riseRateNextList.append(curStock.dayRiseRateCloseFList[i+1])
    ##识别昨日的模型，获取识别结果数据列排序
    riseRateNextList.sort()
    #print riseRateNextList
    
    ##匹配日涨幅
    riseRateCur=curStock.dayRiseRateCloseFList[matchDateIndex]

    numMatch = len(riseRateNextList)
    indexOfRise=1
    if riseRateCur<=riseRateNextList[0]:
        pass 
    elif riseRateCur>=riseRateNextList[-1]:
        indexOfRise=numMatch+1
    else:
        for i in range(numMatch ):
            if riseRateNextList[i]<=riseRateCur<= riseRateNextList[i+1]:
                indexOfRise= i
                break
    #print riseRateCur, indexOfRise
    ##计算匹配日涨幅的位置
    moodIndex =100* float(indexOfRise) / ( numMatch + 1 )
    
    ##计算量能，根据量能修正昨日市场情绪参数
    volEnergeRate = float(curStock.dayTradeVolumeFList[matchDateIndex])/ curStock.dayTradeVolumeFList[matchDateIndex-1]
    
    ##修正市场情绪修正算法
    ##市场情绪通过量能做参数做调整修正，如果是缩量 如果是下跌就X倒数，
    # print volEnergeRate
    if volEnergeRate<1 and curStock.dayRiseRateCloseFList[matchDateIndex]>0:
        moodIndex =  moodIndex * volEnergeRate
    if volEnergeRate<1 and curStock.dayRiseRateCloseFList[matchDateIndex]>0:
        moodIndex =  moodIndex * 1/volEnergeRate
    
    ##通过5日均线修正市场情绪指数
    ## 收盘价大于5日均线
    if curStock.dayPriceClosedArray[matchDateIndex]>=curStock.day5PriceAverageArray[matchDateIndex]:
        if moodIndex<25:
            moodIndex=moodIndex+20
        if 25<=moodIndex<35:
            moodIndex=moodIndex+15
        if 35<=moodIndex<45:
            moodIndex=moodIndex+10
        if 45<=moodIndex<50:
            moodIndex=moodIndex+5
        ##如果最低价小于五日均线
        if curStock.dayRiseRateLowestFList[matchDateIndex]<=curStock.day5PriceAverageArray[matchDateIndex]:
            moodIndex=moodIndex-10
    ## 收盘价小于5日均线
    if curStock.dayPriceClosedArray[matchDateIndex]<=curStock.day5PriceAverageArray[matchDateIndex]:
        if moodIndex>=75:
            moodIndex=moodIndex-20
        if 75>moodIndex>=65:
            moodIndex=moodIndex-15
        if 65>moodIndex>=55:
            moodIndex=moodIndex-10
        if 55>moodIndex>=50:
            moodIndex=moodIndex-5
        ##如果最高价大于五日均线
        if curStock.dayRiseRateHighestFList[matchDateIndex] >= curStock.day5PriceAverageArray[matchDateIndex]:
            moodIndex=moodIndex+10
    
    ##根据数据列计算市场情绪指数
    return moodIndex
    

##计算市场风险指数
def calMarketRiskIndex(curStock,moodIndex,kMatchIndexList):
    ##利用市场情绪指数和大于1和小于-1的参数个数来评估市场风险。
    ##风险级别 5 为最大 
    marketRiskIndex = 5- moodIndex/20
    riseRateNextList=[]
    for i in kMatchIndexList:
        riseRateNextList.append(curStock.dayRiseRateCloseFList[i+1])
    
    value_smaller_1=len(filter(lambda x:x<=-1,riseRateNextList))
    value_bigger1=len(filter(lambda x:x>=1,riseRateNextList))
    
    ## 用小于-1的大盘指数修正，越大风险越大
    if value_bigger1 > value_smaller_1:
        marketRiskIndex = marketRiskIndex - 0.5
    if value_bigger1 < value_smaller_1:
        marketRiskIndex = marketRiskIndex + 0.5 
    return marketRiskIndex

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
    addInforLine(inforLine)
    
    kNum=3 ##需要分析的K线天数
    bias=0.5 ##涨幅取值范围，个股用1，大盘指数用0.5
    if curStock.stockID not in ["999999"] :
        bias=1.0
    
    inforLine="-"*8+u"最近交易日的相关数据："
    addInforLine(inforLine)
    
    lineWritedList.append(u"日期[星期]    \t涨幅\t最大涨幅\t最小涨幅\t量比\t波动幅度\t")
    for i in range(matchDateIndex+1-kNum,matchDateIndex+1): ##循环指数起始比匹配指数少1
        weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday() 
        resultLine=u"{}[{}]\t{}\t{}\t{}\t{}\t{}".format(curStock.dayStrList[i],weekDay,curStock.dayRiseRateCloseFList[i], curStock.dayRiseRateHighestArray[i], curStock.dayRiseRateLowestFList[i], \
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
	
    print("-"*72)
    print(u"计算市场情绪指数")
    moodIndex = calMoodIndexFromRecogitionPattern(curStock,iTradeDay,kNum,matchDateIndex,bias)
    inforLine = u"昨日市场情绪指数{:.2f}".format(moodIndex)
    print (inforLine) 
    addInforLine(inforLine)
    
    print("-"*72)
    print(u"市场风险指数")
    marketRiskIndex = calMarketRiskIndex(curStock,moodIndex,kPatternList)
    inforLine = u"市场风险指数{:.2f}".format(marketRiskIndex)
    print (inforLine) 
    addInforLine(inforLine)

dirPatternRec = "patternRecDir"

def mainAppCall(strDate=""):
    del configOS.patternRecDateListSH[:]
    del configOS.patternRecDateListSZ[:]
    del configOS.patternRecDateListCYB[:]

    for stockID in configOS.stockIDMarketList: 
        curStock=Cstock.Stock(stockID)
        recogitionPatternByDateStr(curStock,strDate) 

    configOS.updatePetternRectDateList()

    for line in lineWritedList:
        print line
    
    dayStr=strDate.replace("/","")
    goalFilePath= os.path.join( dirPatternRec, dayStr+".txt" ) ##输出文件名
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    os.startfile(goalFilePath)

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


