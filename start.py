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

##需要从配置文件中读取不同周期的极值，以便计算压力位和支撑位
def calResistLine(cyclePeriod,keyPoint):
    resistLine=cycleLow+(cycleHigh-cycleLow)*keyPoint
    return resistLine

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

    print(u"-"*80)
    ## 1. 首先要做趋势分析！趋势分为长期，中期，短期趋势
    print(u"1-趋势分析")
    print (u"\n"+"#"*80)
    print(u"1.1-分析两市总市值和GDP的关系")
    gdp2014=float(config.get("GDP","2014"))
    ##此处应该设计必须成输入！
    AB_SH=29.0
    AB_SZ=20.6
    print (u"股市与GDP值比{:.2f}".format((AB_SH+AB_SZ)/gdp2014))

##  分析近期走势
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

    ## 2.空间目标分析，也就是点位预测，在点位空间内控制仓位
    print(u"2-时空分析")
    ##分析当前点位在20日均线和120日均线的压力或者支撑线，50%，33%分割。
    ##需要从配置文件中读取不同周期的极值，以便计算压力位和支撑位
    print (u"\n"+"#"*80+"关键点位提示分析：")
    for period in [20,120]:
        cycle=config.get("cycle","cycle"+str(period))
        cycleHigh=float(cycle.split(":")[0])
        cycleLow=float(cycle.split(":")[1])
        for keyPoint in [0.33,0.5]:
            resistLinePoint=cycleLow+(cycleHigh-cycleLow)*keyPoint
            print(u"{}日 低点:{}，高点:{}，{}线:{}".format(period,cycleLow,cycleHigh,keyPoint,resistLinePoint))
            if(abs(curStock.dayPriceClosedFList[-1]-resistLinePoint)<=50):
                print(u"注意压力位！")
    
    print (u"\n"+"#"*80+"关键时间点分析：")
   
    for period in [10,20,30,60,120]:
        indexHighPoint=curStock.dayPriceHighestFList.index(max(curStock.dayPriceHighestFList[-period:-1]))
        indexLowPoint=curStock.dayPriceLowestFList.index(min(curStock.dayPriceLowestFList[-period:-1]))
        print(u"{}日最高点{}，出现日期{}，距今日{}个交易日".format(period,curStock.dayPriceHighestFList[indexHighPoint], \
                curStock.dayStrList[indexHighPoint],len(curStock.dayStrList)-1-indexHighPoint))
        print(u"{}日最低点{}，出现日期{}，距今日{}个交易日".format(period,curStock.dayPriceLowestFList[indexLowPoint], \
                curStock.dayStrList[indexLowPoint],len(curStock.dayStrList)-1-indexLowPoint))

## 3.仓位控制和仓位止损控制
    print("-"*80)
    print(u"3-仓位管理")
    print(u"3-1 长线资金控制在仓位的35%，在确定大底时进入，持股时间到顶部回撤时撤出，买卖点需要再研究。现在的港股ETF就是长线资金，暂时不动的。坚决不倒腾。高位10%止赢。尽量选ETF品种。")
    print(u"3-2 中线资金控制在仓位的35%，在中期底部可以适当倒腾。但是仓位保持控制，做主题投资。高抛低吸，但是尽量减少操作。")
    print(u"3-3 短线资金控制在仓位的10%，适度追涨停板。但是 一定要盘面稳定，主题鲜明。")
    print(u"3-4 留20%活动资金")
##长线止损
##中线止损
##短线止损
    print(u"3-4 短线止损，如果买入股票当日没有按照自己思路走，次日上午11：30前3%内严格止损。")

## 4.日内操作预测，包括K线识别，当日交易原则等等
    print(u"4-操作建议")
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
   
    print("$"*72)
    print ("-"*8+u"三日K线组合识别系统：")
    print ("-"*8+u"最近交易日的相关数据：")

    print("$"*72)
    
##  均线买入价设计

##  止损位设计
    mymain()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
