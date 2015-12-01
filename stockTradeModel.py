# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Ccomfunc
import numpy as np
import Cstock
import stockPatternRecognition
import configOS
import scipy.optimize as optimize



def main(curStock):
    print ("买卖的目的：1 建仓 2 T价差 3 控制仓位 4 止损")
    print ("卖的条件：1 价格到位 2 时间点")
    print ("做T价格计算，做t是宁可错过，不能做错的方案，一定要有价差才能买入。。")
    print ("-"*72)
   
##  短线资金量及进出原则。

## 买入价一定要 超出买入预期，卖出价要降标准 

    
##----中线资金量选股标的及进出原则计算模块
    ## 利用匹配日求取买入价
    ##用最近的一个匹配日的最低价的涨幅
    print("-"*72)
    print("\n中线资金计算：")
    print("-"*72)
#    patternRecCalTPrice(curStock,dayRadioLinkPriceLowArray)
##----模式识别法买卖价计算模块
  

##----长线资金量计算模块
##----end 长线资金量计算模块
    
    
##----最优化方法买卖价

    print("-"*72)
##----市场情绪法买卖价模块
    print("-"*72)
    print("\n市场情绪法计算：")
    print("-"*72)
##上涨
    if curStock.dayRiseRateArray[-1]>0:
        if 1.5<=curStock.dayRadioLinkOfTradeVolumeArray[-1]:
            print("放巨量上涨。")
        if 1<curStock.dayRadioLinkOfTradeVolumeArray[-1]<1.5:
            print("微放量上涨。")
        if curStock.dayRadioLinkOfTradeVolumeArray[-1]<1:
            print("缩量上涨。")
##下跌
    if curStock.dayRiseRateArray[-1]<0:
        if 1.5<=curStock.dayRadioLinkOfTradeVolumeArray[-1]:
            print("巨放量下跌。")
        if 1<curStock.dayRadioLinkOfTradeVolumeArray[-1]<1.5:
            print("微放量下跌。")
        if curStock.dayRadioLinkOfTradeVolumeArray[-1]<1:
            print("缩量下跌。")
    marketMood=1
    if marketMood<=0.5:
        print("3日T均价{:.2f}".format(priceLow3days*0.5+priceClose3days*0.5))

##----市场情绪法买卖价模块

    
    print ("严格的执行止损方案。")

if __name__=="__main__":
    
    print("\n"+"#"*80)
    
    print ("严格的执行止损方案。")
    print ("手里的票不要超过5支。")
    print ("严格的仓位控制")
    
    startClock=time.clock() ##记录程序开始计算时间
    for stockID in configOS.stockIDList:
        curStock=Cstock.Stock(stockID)
        curStock.list2array()
        main(curStock)
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
