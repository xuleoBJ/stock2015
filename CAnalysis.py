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
   
    
    numTradeDay=100
    print("分析最近"+str(numTradeDay)+"交易日:"+ curStock.dateStrList[-numTradeDay]+"-" +curStock.dateStrList[-1])
    for scale in range(-9,0):
        up=0
        down=0
        for i in range(-numTradeDay,-1):
            if curStock.riseRateFList[i]<=scale  and  curStock.tradeVolumeFList[i]<=curStock.tradeVolumeFList[i-1]:
                if curStock.priceCloseingFList[i+1]>curStock.priceCloseingFList[i]:
                    up=up+1
                else:
                    down=down+1
        print("如果当日上涨"+str(scale)+"%，次个交易日上涨"+str(up)+"，下跌天数"+str(down))
   
    for scale in range(0,10):
        up=0
        down=0
        for i in range(-numTradeDay,-1):
            if curStock.riseRateFList[i]>=scale and  curStock.tradeVolumeFList[i]>= curStock.tradeVolumeFList[i-1] :
                if curStock.priceCloseingFList[i+1]> curStock.priceCloseingFList[i]:
                    up=up+1
                else:
                    down=down+1
        print("如果当日上涨"+str(scale)+"%，次个交易日上涨"+str(up)+"，下跌天数"+str(down))
  

    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


