# -*- coding: utf-8 -*-
import datetime,time
import ConfigParser
import Cstock
import Ccomfunc
import stockAnalysis

def mymain():
    pass

if __name__ == "__main__":
    
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    stockID=config
    startClock=time.clock() ##记录程序开始计算时间
    Ccomfunc.printInfor()
    curStock=Cstock.Stock(stockID)
    stockAnalysis.trend(curStock)
    ##分析当前点位在20日均线和120日均线的压力或者支撑线，50%，33%分割。
    print (u"关键点位提示分析：")
    print (u"正在进行趋势分析：")
    for days in [3,5,8,13,21,34,55,89,144]:
	 Ccomfunc.printCalTrend(curStock,-days)
    mymain()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
