# coding = utf-8   
import os
import shutil
import time
import datetime
import math
import Cstock
import sys

reload(sys)
sys.setdefaultencoding('gbk')


lineWrited=[]

def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

if __name__=="__main__":
    print("\n"+"#"*80)
    print (u"控制风险，保持耐心，态度认真。")
    print (u"熊市甚至行情不确定时，最好是尾盘15分钟买卖！")
    print (u"在历史K线中寻找有类似特征信息的日期，因为历史是重复的，错误也是循环的。")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
   
    ##读取上证指数数据
    ##shStock=Cstock.StockSH()
    

    ##读取股票代码，存储在curStock里
    stockID="999999"
    curStock=Cstock.Stock(stockID)
    
    ##输出文件名
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    fileWrited.write(stockID+'\n')

    ##设置分析周期
    iDaysPeriodUser=1000
    if stockID=="999999":
        iDaysPeriodUser=len(curStock.dateStrList)
    ##起始分析日期 dateStrStart
    dateStrStart=curStock.dateStrList[-iDaysPeriodUser]
    ##终了分析日期 dateStrEnd
    dateStrEnd=curStock.dateStrList[-1]

    print (u"正在查找历史K线日期：！！！！日期选完，请注意看K线趋势，同时注意成交量的表现：")
    ##需要添加日期选择，

    ## 手动设置查找条件
    print (u"手动条件查找历史K线：")
    riseRate_i=int(curStock.riseRateFList[-1])
    riseRate_i_1=int(curStock.riseRateFList[-1])
    for i in range(-iDaysPeriodUser+2,-1):
        bSelect=False
        if  riseRate_i_1<=curStock.riseRateFList[i-1]<=1+riseRate_i_1 and riseRate_i<=curStock.riseRateFList[i]<=1+riseRate_i:
            bSelect=True
        if  bSelect==True:
            weekDay=convertDateStr2Date(curStock.dateStrList[i]).weekday()+1 
            print(curStock.dateStrList[i],"weekDay_"+str(weekDay),"RiseRateofNextTradeDay: "+str(curStock.riseRateFList[i+1]))
            print("_"*30+"riseRate",curStock.riseRateFList[i-2],curStock.riseRateFList[i-1],curStock.riseRateFList[i])
            print("_"*30+"turnOverRate=",curStock.riseOfTurnOverFList[i-2],curStock.riseOfTurnOverFList[i-1],curStock.riseOfTurnOverFList[i-1])
    
    
    ## 自动设置查找条件
    print (u"根据涨幅，自动条件查找历史K线：")
     ## 是否考虑成交量增加或者减少，1考虑 0 不考虑
    isConsiderVOlume=0 
    
    kDays=3 ##需要分析的K线天数
    bias=0.5 ##涨幅取值范围，个股用1，大盘指数用0.5
    if stockID!="999999":
        bias=1.0
    
    for i in range(kDays):
        weekDay=convertDateStr2Date(curStock.dateStrList[-kDays+i]).weekday()+1 ##老外的weekDay比我们少一天，周一是0
        print(curStock.dateStrList[-kDays+i],"weekDay_"+str(weekDay),"rate="+str(curStock.riseRateFList[-kDays+i]),"turnOverRate="+str(curStock.riseOfTurnOverFList[-kDays+i]))

    ##根据涨幅选择历史K线
    for i in range(-iDaysPeriodUser+kDays,-1):
	    iCount=0
	    bSelect=True
	    while iCount<=kDays-1 and bSelect==True:
		    valueRate=math.floor(curStock.riseRateFList[-iCount-1]/bias)*bias
		    if not valueRate<=curStock.riseRateFList[i-iCount]<=valueRate+bias:
			    bSelect=False
		    ##成交量要同步增加或者减少,条件是考虑成交量筛选，成交量大于0，同时 成交量涨幅同时增加或者同时减少，用除法表示同步
		    if isConsiderVOlume==1 and curStock.riseOfTradeVolumeFList[i-iCount]>0 and \
                        curStock.riseOfTradeVolumeFList[-iCount-1]/curStock.riseOfTradeVolumeFList[i-iCount]<0: 
			    bSelect=False
		    iCount=iCount+1
	    if bSelect==True:
                weekDay=convertDateStr2Date(curStock.dateStrList[i]).weekday()+1 ##老外的weekDay比我们少一天，周一是0
                print(curStock.dateStrList[i],"weekDay_"+str(weekDay),curStock.riseRateFList[i-2],curStock.riseRateFList[i-1],curStock.riseRateFList[i],\
                      "turnOverRate=",curStock.riseOfTurnOverFList[i-2],curStock.riseOfTurnOverFList[i-1],curStock.riseOfTurnOverFList[i-1],\
                      "RiseRateofNextTradeDay: "+str(curStock.riseRateFList[i+1]))
    
    ##增加振幅，选择历史K线 
    print (u"根据震动幅度，自动条件查找历史K线：")
    for i in range(kDays):
        weekDay=convertDateStr2Date(curStock.dateStrList[-kDays+i]).weekday()+1 
        print(curStock.dateStrList[-kDays+i],u"星期",str(weekDay),u"振幅="+str(curStock.waveRateFList[-kDays+i]),u"成交量="+str(curStock.riseOfTurnOverFList[-kDays+i]))
    for i in range(-iDaysPeriodUser+kDays,-1):
	    iCount=0
	    bSelect=True
	    while iCount<=kDays-1 and bSelect==True:
		    valueRate=math.floor(curStock.waveRateFList[-iCount-1]/bias)*bias
		    if not valueRate<=curStock.waveRateFList[i-iCount]<=valueRate+bias:
			    bSelect=False
		    iCount=iCount+1
	    if bSelect==True:
                weekDay=convertDateStr2Date(curStock.dateStrList[i]).weekday()+1 ##老外的weekDay比我们少一天，周一是0
                print(curStock.dateStrList[i],"weekDay_"+str(weekDay),curStock.waveRateFList[i-2],curStock.waveRateFList[i-1],curStock.waveRateFList[i],\
                      "turnOverRate=",curStock.riseOfTurnOverFList[i-2],curStock.riseOfTurnOverFList[i-1],curStock.riseOfTurnOverFList[i-1],\
                      "RiseRateofNextTradeDay: "+str(curStock.waveRateFList[i+1]))
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


