## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import numpy


from scipy.stats.stats import pearsonr

##������Ʊ��������Ƶ�ͬ����
def analysisSynchronization(numOfTradeDays,curStock,shStock):
    dateStrStart=curStock.dayStrList[-numOfTradeDays]
    dateStrEnd=curStock.dayStrList[-1]
## get analysis indexStartDay and indexEndDay by dayStrList
    indexStart=curStock.dayStrList.index(dateStrStart)
    indexEnd=curStock.dayStrList.index(dateStrEnd)
    print("-"*50)
    print (str(numOfTradeDays)+"�������������ͬ���Է���:��ʼ�գ�"+dateStrStart+"��"+dateStrEnd)
    waveSHFList=[]
    waveStockFList=[]
## ͨ�������ҵ�����ͬ��index
    for i in range(indexStart,indexEnd):
        dateStrSH=curStock.dayStrList[i]
        indexSH=shStock.shDateStrList.index(dateStrSH)
        r1=round(100*(curStock.priceCloseingFList[i]-curStock.priceCloseingFList[i-1])/curStock.priceCloseingFList[i-1],2)
        waveStockFList.append(r1)
        rSH=round(100*(shStock.shPriceCloseingFList[indexSH]-shStock.shPriceCloseingFList[indexSH-1])/shStock.shPriceCloseingFList[indexSH-1],2)
        waveSHFList.append(rSH)
    print("���ϵ����"+str(pearsonr(waveSHFList,waveStockFList)))
    

if __name__=="__main__":
    print("\n"+"-"*80)
    print ("�����з��գ�����������Ļ��ᣬ������Ҫ���ģ�����̬��Ҫ���档")
    print("\n"+"-"*80)
    
    startClock=time.clock() ##��¼����ʼ����ʱ��
    
    shStock=Cstock.StockSH()
    
    stockID="601766"
    curStock=Cstock.Stock(stockID)

    for numOfTradeDays in [5,10,20,30]:
        analysisSynchronization(numOfTradeDays,curStock,shStock)   
  

    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


