# coding = utf-8   
import os
import shutil
import time
import datetime
import math
import Cstock
import sys
import Ccomfunc

def printResult(curStock,indexList):
    for index in indexList: 
        weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[index]).isoweekday() 
        print u"{0},星期{1},前3日涨幅{2},{3},{4},量幅{5},{6},{7},次日涨幅{8},次日开盘{9:.2f}".format(curStock.dayStrList[index],weekDay,\
                        curStock.dayRiseRateFList[index-2],curStock.dayRiseRateFList[index-1],curStock.dayRiseRateFList[index],\
                        curStock.dayRiseOfTurnOverFList[index-2],curStock.dayRiseOfTurnOverFList[index-1],curStock.dayRiseOfTurnOverFList[index],\
                        curStock.dayRiseRateFList[index+1],curStock.dayOpenRateFList[index+1])
#                for intervalDay in [-3,-5,-8,-13,-21,-34,-55,-89]:
#                    print (u"对比日{}日涨幅{:.2f}，当前{:.2f}".format(intervalDay,Ccomfunc.calRiseRateInterval(curStock,i,intervalDay), Ccomfunc.calTrend(curStock,intervalDay))) ##注意这里用的是负指数
        for intervalDay in [3,5,8]:
            print (u"{}日涨幅{:.2f}".format(intervalDay,Ccomfunc.calRiseRateInterval(curStock,index,intervalDay)))


def patternRecByRiseRate(curStock,iTradeDay,kNum,bias=0.3):
    ##根据涨幅进行历史K线模式识别,iTradeDay curStock周期，kNum是K线组合个数
    ##需要增加从某一天开始的模式
    kMatchIndexList=[] ##匹配的模式个数
    print ("-"*8+u"根据前{}涨幅，自动设置条件，模式识别：".format(kNum))
    for i in range(-iTradeDay+kNum,-1):
	    iCount=0
	    bSelect=True
	    while iCount<=kNum-1 and bSelect==True:
		    ## 考虑涨幅
		    valueRate=math.floor(curStock.dayRiseRateFList[-iCount-1]/bias)*bias
		    if not valueRate<=curStock.dayRiseRateFList[i-iCount]<=valueRate+bias:
			    bSelect=False
            ##考虑成交量
		    iCount=iCount+1
	    if bSelect==True:
		    kMatchIndexList.append(i)
    return kMatchIndexList

## 在利用K线组合的匹配的结果中，用开盘价进行过滤 
def patternRecByPriceOpen(curStock,kMatchIndexList,kNum,bias=0.3):
    ##根据前几日涨幅及开盘价进行历史K线模式识别：
    selectList=[]
    for index in kMatchIndexList:
	    iCount=0
	    valueRate=math.floor(curStock.dayPriceOpenFList[-iCount-1]/bias)*bias
	    if  valueRate<=curStock.dayPriceClosedFList[index-iCount]<=valueRate+bias: 
		     selectList.append(index)
	    iCount=iCount+1
    return selectList

## 在利用K线组合的匹配的结果中，用收盘价进行过滤 
def patterRecByPriceClose(curStock,kMatchIndexList,kNum,bias=0.3):
    selectList=[]
    for index in kMatchIndexList:
	    iCount=0
	    valueRate=math.floor(curStock.dayPriceClosedFList[-iCount-1]/bias)*bias
	    if  valueRate<=curStock.dayPriceClosedFList[index-iCount]<=valueRate+bias: 
		     selectList.append(index)
	    iCount=iCount+1
    return selectList

## 在利用K线组合的匹配的结果中，用波动幅度进行过滤 
def patternRecByRiseWave(curStock,kMatchIndexList,kNum,bias=0.3):
    selectList=[]
    for index in kMatchIndexList:
	    iCount=0
	    valueRate=math.floor(curStock.dayWaveRateFList[-iCount-1]/bias)*bias
	    if  valueRate<=curStock.dayWaveRateFList[index-iCount]<=valueRate+bias: 
		     selectList.append(index)
	    iCount=iCount+1
    return selectList

def patterRecByVolume(curStock,iTradeDay,kNum):
    ##成交量要同步增加或者减少,条件是考虑成交量筛选，成交量大于0，同时 成交量涨幅同时增加或者同时减少，用除法表示同步
    selectList=[]
    for index in kMatchIndexList:
	    iCount=0
	    valueRate=math.floor(curStock.dayWaveRateFList[-iCount-1]/bias)*bias
	    if  valueRate<=curStock.dayWaveRateFList[index-iCount]<=valueRate+bias: 
		     selectList.append(index)
	    iCount=iCount+1
    return selectList
    pass
#		    if isConsiderVOlume==1 and curStock.dayRadioLinkOfTradeVolumeFList[i-iCount]>0 and \
#                        curStock.dayRadioLinkOfTradeVolumeFList[-iCount-1]/curStock.dayRadioLinkOfTradeVolumeFList[i-iCount]<0: 
#			    bSelect=False

def patterRecByHandSet(curStock,iTradeDay,kNum):
    ## 手动设置查找条件
    print ("-"*8+u"手动设置条件查找历史K线：")
    riseRate_i=int(curStock.dayRiseRateFList[-1])
    riseRate_i_1=int(curStock.dayRiseRateFList[-2])
    for i in range(-iTradeDay+2,-1):
        bSelect=False
        ##自动设置条件，用最后两个交易日做基准
        if  riseRate_i_1<=curStock.dayRiseRateFList[i-1]<=1+riseRate_i_1 and riseRate_i<=curStock.dayRiseRateFList[i]<=1+riseRate_i:
        ##手工设置if条件
#        if  curStock.dayRiseRateFList[i-1]<=0 and 5<=curStock.dayRiseRateFList[i]<=7:
            bSelect=True
        if  bSelect==True:
            weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday() 
            print(curStock.dayStrList[i],"weekDay_"+str(weekDay),"RiseRateofNextTradeDay: "+str(curStock.dayRiseRateFList[i+1]))
            print(u"{},星期{},次日涨幅:{}".format(curStock.dayStrList[i],weekDay,curStock.dayRiseRateFList[i+1]))
            print("_"*30+"riseRate",curStock.dayRiseRateFList[i-2],curStock.dayRiseRateFList[i-1],curStock.dayRiseRateFList[i])
            print("_"*30+"turnOverRate=",curStock.dayRiseOfTurnOverFList[i-2],curStock.dayRiseOfTurnOverFList[i-1],curStock.dayRiseOfTurnOverFList[i-1])

stockID="999999"

if __name__=="__main__":
    
    ##模式识别的方法，如果最近3天的没有 可以用前三天的往后推
    startClock=time.clock() ##记录程序开始计算时间
   
    ##读取股票代码，存储在curStock里
    curStock=Cstock.Stock(stockID)

    lineWritedList=[]
    lineWritedList.append(stockID)

    ##设置分析周期,缺省为1000，是4年的行情
    iTradeDay=1000
    if stockID=="999999":
        iTradeDay=len(curStock.dayStrList)
    ##起始分析日期 dateStrStart
    dateStrStart=curStock.dayStrList[-iTradeDay]
    ##终了分析日期 dateStrEnd
    dateStrEnd=curStock.dayStrList[-1]

    print("-"*72)
    print ("-"*8+u"正在查找历史K线日期：！！！！日期选完，请注意看K线趋势，同时注意成交量的表现：")
    
    ## 是否考虑成交量增加或者减少，1考虑 0 不考虑
    isConsiderVOlume=0 
    
    kNum=3 ##需要分析的K线天数
    bias=0.5 ##涨幅取值范围，个股用1，大盘指数用0.5
    if stockID!="999999":
        bias=1.0
    
    print("$"*72)
    print ("-"*8+u"涨幅组合识别，三日K线组合识别系统：")
    print ("-"*8+u"最近交易日的相关数据：")
    for i in range(-kNum,0): ##注意用的负指数
        weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday() 
        print(u"{},星期{},涨幅:{}".format(curStock.dayStrList[i],weekDay,curStock.dayRiseRateFList[i]))
    
    indexList=patternRecByRiseRate(curStock,iTradeDay,kNum,bias)
    printResult(curStock,indexList)
    
    print("$"*72)
    print ("-"*8+u"增加收盘价匹配条件：")
    indexList=patterRecByPriceClose(curStock,indexList,kNum)
    printResult(curStock,indexList)

    print("$"*72)
    print ("-"*8+u"增加收盘价开盘价匹配条件：")
    patternRecByPriceOpen(curStock,indexList,kNum)
    
    print("$"*72)
    print ("-"*8+u"增加振幅匹配条件：")
    patternRecByRiseWave(curStock,indexList,kNum)
    
    print("$"*72)
    print ("-"*8+u"增加成交量匹配条件：")
    print("$"*72)
    for i in range(-kNum,0): ##注意用的负指数
        weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday() 
        print(u"{},星期{},波动幅度:{},涨幅：{}".format(curStock.dayStrList[i],weekDay,curStock.dayWaveRateFList[i],curStock.dayRiseRateFList[i]))
	
    
    ##输出文件名
    goalFilePath='result.txt'
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


