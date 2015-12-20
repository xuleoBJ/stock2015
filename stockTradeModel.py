# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Ccomfunc
import numpy as np
from Cstock import Stock
import stockPatternRecognition
import configOS
import scipy.optimize as optimize

def calTBuy(curStock):
    priceTBuyDic={}
    priceTBuyDic['CloseYesto'] = curStock.dayPriceClosedArray[-1]
    priceTBuyDic['CloseDay5Ave'] = curStock.day5PriceAverageArray[-1]
    priceTBuyDic['CloseDay98'] = curStock.dayPriceClosedArray[-1]*0.98
    priceTBuyDic['Lowest5'] = curStock.dayPriceLowestArray[-5:].min()
    priceTBuyDic['Lowest3'] = curStock.dayPriceLowestArray[-3:].min()
    for key,value in sorted(priceTBuyDic.items(), key=lambda x:-x[1]):
        print key,"\t",round(value,2)
   
##  周线趋势必须向上，判断原则 MACD RSI 

##  美股跌1.5以上，做T的级别降一级。

if __name__=="__main__":
    startClock=time.clock() ##记录程序开始计算时间
    print ("严格的执行止损方案。")
    curStock=Stock('002285')
    calTBuy(curStock)
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
