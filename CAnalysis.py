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
    
    shStock=Cstock.StockSH()
    
    stockID="601318"
    curStock=Cstock.Stock(stockID)
   
    
    numTradeDay=200
    print("分析最近"+str(numTradeDay)+"交易日:"+ curStock.dateStrList[-numTradeDay]+"-" +curStock.dateStrList[-1])
    
    numdays=0
    up=0
    down=0
    for i in range(-numTradeDay,-1):
        if curStock.tradeVolumeFList[i]>=curStock.tradeVolumeFList[i-1]>=curStock.tradeVolumeFList[i-2] :
                numdays=numdays+1
                if curStock.priceCloseingFList[i+1]>curStock.priceCloseingFList[i]:
                    up=up+1
                else:
                    down=down+1
    print("交易量连涨3天交易日个数"+str(numdays)+"，次个交易日上涨"+str(up)+"，下跌天数"+str(down))



    for scale in range(-9,0):
        numdays=0
        up=0
        down=0
        for i in range(-numTradeDay,-1):
            ##curStock.tradeVolumeFList[i]<=curStock.tradeVolumeFList[i-1]
            if curStock.riseRateFList[i]<=scale :
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
            ##  curStock.tradeVolumeFList[i]>= curStock.tradeVolumeFList[i-1]
            if curStock.riseRateFList[i]>=scale  :
                numdays=numdays+1
                if curStock.priceCloseingFList[i+1]> curStock.priceCloseingFList[i]:
                    up=up+1
                else:
                    down=down+1
        print("当日上涨"+str(scale)+"%交易日个数"+str(numdays)+"，次个交易日上涨"+str(up)+"，下跌天数"+str(down))
  

    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


