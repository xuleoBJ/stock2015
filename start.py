# -*- coding: utf-8 -*-
import os
import datetime,time
import ConfigParser
import Cstock
import Ccomfunc
import stockAnalysis
import stockPatternRecognition

def mymain():
    pass

def calResistLine(cyclePeriod):
    cycle=config.get("cycle","cycle"+str(cyclePeriod))
    cycleHigh=float(cycle.split(":")[0])
    cycleLow=float(cycle.split(":")[1])
    resistLine50=cycleLow+(cycleHigh-cycleLow)*0.5
    resistLine33=cycleLow+(cycleHigh-cycleLow)*0.33
    print (u"{}日 低点:{}，高点:{}，.50线:{}，.33线:{}".format(cyclePeriod,cycleLow,cycleHigh,resistLine50,resistLine33))

if __name__ == "__main__":
    startClock=time.clock() ##记录程序开始计算时间
## 改变路径到工作目录 
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print os.path.curdir
## 读取配置文件，获取相关信息，活得股票ID,实例化 curStock
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    stockID=config.get("stock","stockID")
    Ccomfunc.printInfor()
    curStock=Cstock.Stock(stockID)

##  分析两市总市值和GDP的关系
    print (u"\n"+"#"*80)
    gdp2014=float(config.get("GDP","2014"))
    AB_SH=27.7
    AB_SZ=19.2
    print (u"股市与GDP值比{:.2f}".format((AB_SH+AB_SZ)/gdp2014))

##分析当前点位在20日均线和120日均线的压力或者支撑线，50%，33%分割。
    print (u"\n"+"#"*80+"关键点位提示分析：")
    for period in [20,120]:
         calResistLine(period)

##  分析近期走势
    print (u"\n"+"#"*80)
    stockAnalysis.trend(curStock)
   
    print (u"\n"+"#"*80+"正在进行趋势分析：")
    for days in [3,5,8,13,21,34,55,89,144]:
	 Ccomfunc.printCalTrend(curStock,-days)

##  峰值研究

##  分析近年同期走势
    print (u"过去3年同期交易日走势,近期走势：")
    today=datetime.date.today()
    for i in [1,2,3]:
        todayLastYear=today-datetime.timedelta(days=365*i) ##不准确但是可行
        wordsPrint=[]
        for item in curStock.dateList:
            if todayLastYear-datetime.timedelta(days=1)<=item:
                _index=curStock.dateList.index(item)
                wordsPrint.append(curStock.dayStrList[_index])
                for days in [3,5,8,13]:
                    wordsPrint.append("{}日涨幅{:.2f}".format(days,Ccomfunc.calRiseRateInterval(curStock,_index,days)))
                break
   
        print u"{}年同期涨幅:{}".format(todayLastYear.year,"\t".join(wordsPrint))

##  K线模式识别
    
    ##设置分析周期,缺省为1000，是4年的行情
    iDaysPeriodUser=1000
    if stockID=="999999":
        iDaysPeriodUser=len(curStock.dayStrList)
    ##起始分析日期 dateStrStart
    dateStrStart=curStock.dayStrList[-iDaysPeriodUser]
    ##终了分析日期 dateStrEnd
    dateStrEnd=curStock.dayStrList[-1]

    print("-"*72)
    print ("-"*8+u"正在查找历史K线日期：！！！！日期选完，请注意看K线趋势，同时注意成交量的表现：")
    
    ## 是否考虑成交量增加或者减少，1考虑 0 不考虑
    isConsiderVOlume=0 
    
    kDays=3 ##需要分析的K线天数
    bias=0.5 ##涨幅取值范围，个股用1，大盘指数用0.5
    if stockID!="999999":
        bias=1.0
    
    print("$"*72)
    print ("-"*8+u"三日K线组合识别系统：")
    print ("-"*8+u"最近交易日的相关数据：")
    for i in range(-kDays,0): ##注意用的负指数
        weekDay=Ccomfunc.convertDateStr2Date(curStock.dayStrList[i]).isoweekday() 
        print(u"{},星期{},涨幅:{}".format(curStock.dayStrList[i],weekDay,curStock.dayRiseRateFList[i]))

    if stockPatternRecognition.patternRecByRiseRate(curStock,iDaysPeriodUser,kDays,bias)<1:
        print(u"三个交易日识别无参照，交易日个数减少为2个识别：")
        stockPatternRecognition.patternRecByRiseRate(curStock,iDaysPeriodUser,kDays-1,bias)

    print("$"*72)
    print ("-"*8+u"K线+开盘价识别系统：")
    valueOpenPrice=-0.27
    stockPatternRecognition.patternRecByPriceOpen(curStock,iDaysPeriodUser,kDays-1,valueOpenPrice)
    
##  均线买入价设计

##  止损位设计

    mymain()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
