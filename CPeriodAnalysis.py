## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import numpy
import Cstock
from scipy.stats.stats import pearsonr

##分析股票与大盘走势的同步性
def analysisSynchronization(numOfTradeDays,curStock,shStock):
    dateStrStart=curStock.dateStrList[-numOfTradeDays]
    dateStrEnd=curStock.dateStrList[-1]
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=curStock.dateStrList.index(dateStrStart)
    indexEnd=curStock.dateStrList.index(dateStrEnd)
    print("-"*50)
    print (str(numOfTradeDays)+"个交易日与大盘同步性分析:开始日："+dateStrStart+"至"+dateStrEnd)
    waveSHFList=[]
    waveStockFList=[]
## 通过日期找到大盘同期index
    for i in range(indexStart,indexEnd):
        dateStrSH=curStock.dateStrList[i]
        indexSH=shStock.shDateStrList.index(dateStrSH)
        r1=round(100*(curStock.priceCloseingFList[i]-curStock.priceCloseingFList[i-1])/curStock.priceCloseingFList[i-1],2)
        waveStockFList.append(r1)
        rSH=round(100*(shStock.shPriceCloseingFList[indexSH]-shStock.shPriceCloseingFList[indexSH-1])/shStock.shPriceCloseingFList[indexSH-1],2)
        waveSHFList.append(rSH)
    print("相关系数："+str(pearsonr(waveSHFList,waveStockFList)))
    

if __name__=="__main__":
    print("\n"+"-"*80)
    print ("股市有风险，股市有无穷的机会，股市需要耐心，股市态度要认真。")
    print("\n"+"-"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
    
    shStock=Cstock.StockSH()
    
    stockID="600196"
    curStock=Cstock.Stock(stockID)

    for numOfTradeDays in [5,10,20,30]:
        analysisSynchronization(numOfTradeDays,curStock,shStock)   
  

    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


