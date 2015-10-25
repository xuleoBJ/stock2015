# -*- coding: utf-8 -*-
import os
import datetime,time
import ConfigParser
import Cstock
import Ccomfunc
import stockAnalysis

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

##  K线模式识别

##  均线买入价设计

##  止损位设计
    mymain()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
