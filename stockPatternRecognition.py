# coding = utf-8   
import os
import shutil
import time
import datetime
import math
import Cstock
import sys
import Ccomfunc

def patternRecByRiseRate(curStock,iDaysPeriodUser,kDays):
    ##根据涨幅进行历史K线模式识别
    numSelect=0
    print ("-"*8+u"根据涨幅，自动设置条件，历史K线模式识别：")
    for i in range(-iDaysPeriodUser+kDays,-1):
	    iCount=0
	    bSelect=True
	    while iCount<=kDays-1 and bSelect==True:
		    valueRate=math.floor(curStock.dayRiseRateFList[-iCount-1]/bias)*bias
		    if not valueRate<=curStock.dayRiseRateFList[i-iCount]<=valueRate+bias:
			    bSelect=False
		    ##成交量要同步增加或者减少,条件是考虑成交量筛选，成交量大于0，同时 成交量涨幅同时增加或者同时减少，用除法表示同步
		    if isConsiderVOlume==1 and curStock.dayRiseOfTradeVolumeFList[i-iCount]>0 and \
                        curStock.dayRiseOfTradeVolumeFList[-iCount-1]/curStock.dayRiseOfTradeVolumeFList[i-iCount]<0: 
			    bSelect=False
		    iCount=iCount+1
	    if bSelect==True:
                numSelect=numSelect+1
                weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday() 
                print u"{0},星期{1},前3日涨幅{2},{3},{4},量幅{5},{6},{7},次日涨幅{8},3日涨幅{9:.2f},5日涨幅{10:.2f},".format(curStock.dayStrList[i],weekDay,\
                        curStock.dayRiseRateFList[i-2],curStock.dayRiseRateFList[i-1],curStock.dayRiseRateFList[i],\
                        curStock.dayRiseOfTurnOverFList[i-2],curStock.dayRiseOfTurnOverFList[i-1],curStock.dayRiseOfTurnOverFList[i],\
                        curStock.dayRiseRateFList[i+1],Ccomfunc.calRiseRateInterval(curStock,i,3),Ccomfunc.calRiseRateInterval(curStock,i,5))
    return numSelect

def patternRecByRiseWave(curStock,iDaysPeriodUser,kDays):
    ##增加振幅，选择历史K线 
    print ("-"*8+u"根据波动动幅度，自动设置条件，K线模式识别：")
    for i in range(-iDaysPeriodUser+kDays,-1):
	    iCount=0
	    bSelect=True
	    while iCount<=kDays-1 and bSelect==True:
		    ##用系数放缩找形态
		    valueRate=math.floor(curStock.dayWaveRateFList[-iCount-1]/bias)*bias
		    if not valueRate<=curStock.dayWaveRateFList[i-iCount]<=valueRate+bias:
			    bSelect=False
		    iCount=iCount+1
	    if bSelect==True:
                weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday() 
                print u"{},星期{},三日波动{},{},{},量幅{},{},{}，涨幅{},{},{},次日涨幅{}".format(curStock.dayStrList[i],weekDay, \
                    curStock.dayWaveRateFList[i-2],curStock.dayWaveRateFList[i-1],curStock.dayWaveRateFList[i], \
                    curStock.dayRiseOfTurnOverFList[i-2],curStock.dayRiseOfTurnOverFList[i-1],curStock.dayRiseOfTurnOverFList[i],\
                    curStock.dayRiseRateFList[i-2],curStock.dayRiseRateFList[i-1],curStock.dayRiseRateFList[i],\
                  curStock.dayRiseRateFList[i+1])


def patterRecByHandSet(curStock,iDaysPeriodUser,kDays):
    ## 手动设置查找条件
    print ("-"*8+u"手动设置条件查找历史K线：")
    riseRate_i=int(curStock.dayRiseRateFList[-1])
    riseRate_i_1=int(curStock.dayRiseRateFList[-2])
    for i in range(-iDaysPeriodUser+2,-1):
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
    
    Ccomfunc.printInfor()
    
    ##模式识别的方法，如果最近3天的没有 可以用前三天的往后推
    print (u"在历史K线中寻找有类似特征信息的日期，因为历史是重复的，错误也是循环的。")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
   
    
    ##读取股票代码，存储在curStock里
    curStock=Cstock.Stock(stockID)

    lineWritedList=[]
    lineWritedList.append(stockID)

    ##设置分析周期,缺省为1000，是4年的行情
    iDaysPeriodUser=1000
    if stockID=="999999":
        iDaysPeriodUser=len(curStock.dayStrList)
    ##起始分析日期 dateStrStart
    dateStrStart=curStock.dayStrList[-iDaysPeriodUser]
    ##终了分析日期 dateStrEnd
    dateStrEnd=curStock.dayStrList[-1]

    print (u"正在进行趋势分析：")
    for days in [3,5,8,13,21,34,55,89,144]:
	 Ccomfunc.printCalTrend(curStock,-days)
    
    print (u"过去3年同期20个交易日走势：")
    today=datetime.date.today()
    for i in [1,2,3]:
        todayLastYear=today-datetime.timedelta(days=365*i) ##不准确但是可行
        print u"{}年同期涨幅：".format(todayLastYear.year)
        for item in curStock.dateList:
            if todayLastYear-datetime.timedelta(days=1)<=item<=todayLastYear+datetime.timedelta(days=10):
                _index=curStock.dateList.index(item)
                print curStock.dayStrList[_index],curStock.dayRiseRateFList[_index]
   
    print (u"根据交易日涨幅查找历史K：")
    bSelect=True
    for days in [3]:
        _riseRate= int(Ccomfunc.calTrend(curStock,days))
        for i in range(-iDaysPeriodUser+days,-1):
            if  _riseRate<=Ccomfunc.calRiseRateInterval(curStock,i,days)<=1+_riseRate:
                bSelect=False
    if  bSelect==True:
        weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday()
        print(curStock.dayStrList[i],"weekDay_"+str(weekDay),"RiseRateofNextTradeDay: "+str(curStock.dayRiseRateFList[i+1]))
        print("riseRate",curStock.dayRiseRateFList[i-2],curStock.dayRiseRateFList[i-1],curStock.dayRiseRateFList[i])
        print("turnOverRate=",curStock.dayRiseOfTurnOverFList[i-2],curStock.dayRiseOfTurnOverFList[i-1],curStock.dayRiseOfTurnOverFList[i-1])


    print("-"*72)
    print ("-"*8+u"正在查找历史K线日期：！！！！日期选完，请注意看K线趋势，同时注意成交量的表现：")
    
    ## 是否考虑成交量增加或者减少，1考虑 0 不考虑
    isConsiderVOlume=0 
    
    kDays=3 ##需要分析的K线天数
    bias=0.5 ##涨幅取值范围，个股用1，大盘指数用0.5
    if stockID!="999999":
        bias=1.0
    
    print("-"*72)
    print ("-"*8+u"最近交易日的相关数据：")
    for i in range(-kDays,0): ##注意用的负指数
        weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday() 
        print(u"{},星期{},涨幅:{}".format(curStock.dayStrList[i],weekDay,curStock.dayRiseRateFList[i]))

    if patternRecByRiseRate(curStock,iDaysPeriodUser,kDays)<1:
        print(u"交易日个数减少为2个")
        patternRecByRiseRate(curStock,iDaysPeriodUser,kDays-1)

    print("-"*72)
    for i in range(-kDays,0): ##注意用的负指数
        weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday() 
        print(u"{},星期{},波动幅度:{},涨幅：{}".format(curStock.dayStrList[i],weekDay,curStock.dayWaveRateFList[i],curStock.dayRiseRateFList[i]))
	
    patternRecByRiseWave(curStock,iDaysPeriodUser,kDays)
    
    ##输出文件名
    goalFilePath='result.txt'
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


