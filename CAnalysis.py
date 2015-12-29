## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import numpy
import Cstock

if __name__=="__main__":
    print("\n"+"-"*80)
    print ("股市有风险，股市有无穷的机会，股市需要耐心，股市态度要认真。")
    print("\n"+"-"*80)
    
    startClock=time.clock() ##记录程序开始计算时间
    
    
    stockID="601318"
    curStock=Cstock.Stock(stockID)
   
    
    numTradeDay=200
    print("分析最近"+str(numTradeDay)+"交易日:"+ curStock.dayStrList[-numTradeDay]+"-" +curStock.dayStrList[-1])
    
    numOfRiseDay=3
    mumOfRiseVolume=3
    
    priceList=[]
##    while numberDay>=0:
##        if curStock.priceCloseingFList[-numberDay-1]>=curStock.priceCloseingFList[-numberDay-2]:
##            priceList.append(1)
##        else:
##            priceList.append(0)

    numdays=0
    up=0
    down=0
    for i in range(-numTradeDay,-1):
        if curStock.dayTradeVolumeFList[i]>=curStock.dayTradeVolumeFList[i-1]>=curStock.dayTradeVolumeFList[i-2] :
                numdays=numdays+1
                if curStock.priceCloseingFList[i+1]>curStock.priceCloseingFList[i]:
                    up=up+1
                else:
                    down=down+1
    print("交易量连涨3天交易日个数"+str(numdays)+"，次个交易日上涨"+str(up)+"，下跌天数"+str(down))

## 连续上涨交易日，次日上涨概率
    for i in range(-numTradeDay,-1):
        if curStock.priceCloseingFList[i]>=curStock.priceCloseingFList[i-1]>=curStock.priceCloseingFList[i-2] \
                and curStock.dayTradeVolumeFList[i]<=curStock.dayTradeVolumeFList[i-1]<=curStock.dayTradeVolumeFList[i-2]:
                numdays=numdays+1
                if curStock.priceCloseingFList[i+1]>curStock.priceCloseingFList[i]:
                    up=up+1
                else:
                    down=down+1
    print("收盘连跌3个交易日且交易量下跌"+str(numdays)+"，次个交易日上涨"+str(up)+"，下跌天数"+str(down))

## 连续上涨幅度，次日上涨概率
    for scale in range(-9,0):
        numdays=0
        up=0
        down=0
        for i in range(-numTradeDay,-1):
            ##curStock.dayTradeVolumeFList[i]<=curStock.dayTradeVolumeFList[i-1]
            if curStock.dayRiseRateCloseFList[i]<=scale :
                numdays=numdays+1
                if curStock.priceCloseingFList[i+1]>curStock.priceCloseingFList[i]:
                    up=up+1
                else:
                    down=down+1
        print("当日上涨"+str(scale)+"%交易日个数"+str(numdays)+"，次个交易日上涨"+str(up)+"，下跌天数"+str(down))
   
    for scale in range(0,10):
        numdays=0
        up=0
        down=0
        for i in range(-numTradeDay,-1):
            ##  curStock.dayTradeVolumeFList[i]>= curStock.dayTradeVolumeFList[i-1]
            if curStock.dayRiseRateCloseFList[i]>=scale  :
                numdays=numdays+1
                if curStock.priceCloseingFList[i+1]> curStock.priceCloseingFList[i]:
                    up=up+1
                else:
                    down=down+1
        print("当日上涨"+str(scale)+"%交易日个数"+str(numdays)+"，次个交易日上涨"+str(up)+"，下跌天数"+str(down))

## 连续最高价与收盘价的幅度
    for scale in range(0,10):
        numdays=0
        up=0
        down=0
        for i in range(-numTradeDay,-1):
            if scale<= (curStock.dayPriceHighestFList[i]-curStock.priceCloseingFList[i])*100/curStock.dayPriceOpenFList[i]<scale+1 :
                numdays=numdays+1
                if curStock.priceCloseingFList[i+1]>curStock.priceCloseingFList[i]:
                    up=up+1
                else:
                    down=down+1
        print("最高价与收盘价幅度差"+str(scale)+"~"+str(scale+1)+"%交易日个数"+str(numdays)+"，次个交易日上涨"+str(up)+"，下跌天数"+str(down))

## 连续最低价与收盘价的幅度
    for scale in range(0,10):
        numdays=0
        up=0
        down=0
        for i in range(-numTradeDay,-1):
            if scale<= (curStock.priceCloseingFList[i]-curStock.dayPriceLowestFList[i])*100/curStock.dayPriceOpenFList[i]<scale+1 :
                numdays=numdays+1
                if curStock.priceCloseingFList[i+1]>curStock.priceCloseingFList[i]:
                    up=up+1
                else:
                    down=down+1
        print("最低价与收盘价幅度差"+str(scale)+"~"+str(scale+1)+"%交易日个数"+str(numdays)+"，次个交易日上涨"+str(up)+"，下跌天数"+str(down))
   

    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


