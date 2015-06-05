## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import numpy
import Cstock
from scipy.stats.stats import pearsonr

##������Ʊ��������Ƶ�ͬ����
def analysisSynchronization(numOfTradeDays,curStock,shStock):
    dateStrStart=curStock.dateStrList[-numOfTradeDays]
    dateStrEnd=curStock.dateStrList[-1]
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=curStock.dateStrList.index(dateStrStart)
    indexEnd=curStock.dateStrList.index(dateStrEnd)
    print("-"*50)
    print (str(numOfTradeDays)+"�������������ͬ���Է���:��ʼ�գ�"+dateStrStart+"��"+dateStrEnd)
    waveSHFList=[]
    waveStockFList=[]
## ͨ�������ҵ�����ͬ��index
    for i in range(indexStart,indexEnd):
        dateStrSH=curStock.dateStrList[i]
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
    
    stockID="600196"
    curStock=Cstock.Stock(stockID)

    for numOfTradeDays in [5,10,20,30]:
        analysisSynchronization(numOfTradeDays,curStock,shStock)   
  

    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


