# -*- coding: utf-8 -*-
import datetime,time
import ConfigParser
import Cstock
import Ccomfunc
import stockAnalysis

def getStockID():
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    return config.get('stock','stockID')


def mymain():
    stockIDList = getStockID().split(",")


if __name__ == "__main__":
    
    startClock=time.clock() ##记录程序开始计算时间
    Ccomfunc.printInfor()
    curStock=Cstock.Stock(getStockID())
    stockAnalysis.trend(curStock)
    mymain()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
