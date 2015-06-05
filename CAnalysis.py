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
    print ("�����з��գ�����������Ļ��ᣬ������Ҫ���ģ�����̬��Ҫ���档")
    print("\n"+"-"*80)
    
    startClock=time.clock() ##��¼����ʼ����ʱ��
    
    shStock=Cstock.StockSH()
    
    stockID="601318"
    curStock=Cstock.Stock(stockID)
   
    
    numTradeDay=100
    print("�������"+str(numTradeDay)+"������:"+ curStock.dateStrList[-numTradeDay]+"-" +curStock.dateStrList[-1])
    for scale in range(-9,0):
        up=0
        down=0
        for i in range(-numTradeDay,-1):
            if curStock.riseRateFList[i]<=scale  and  curStock.tradeVolumeFList[i]<=curStock.tradeVolumeFList[i-1]:
                if curStock.priceCloseingFList[i+1]>curStock.priceCloseingFList[i]:
                    up=up+1
                else:
                    down=down+1
        print("�����������"+str(scale)+"%���θ�����������"+str(up)+"���µ�����"+str(down))
   
    for scale in range(0,10):
        up=0
        down=0
        for i in range(-numTradeDay,-1):
            if curStock.riseRateFList[i]>=scale and  curStock.tradeVolumeFList[i]>= curStock.tradeVolumeFList[i-1] :
                if curStock.priceCloseingFList[i+1]> curStock.priceCloseingFList[i]:
                    up=up+1
                else:
                    down=down+1
        print("�����������"+str(scale)+"%���θ�����������"+str(up)+"���µ�����"+str(down))
  

    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


