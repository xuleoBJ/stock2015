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

def calTBuy(curStock,strDate=""):
    matchDateIndex = Ccomfunc.getIndexByStrDate(curStock,strDate)
    priceTBuyDic={}
    priceTBuyDic['CloseYesto'] = curStock.dayPriceClosedArray[matchDateIndex]
    priceTBuyDic['CloseDay5Ave'] = curStock.day5PriceAverageArray[matchDateIndex]
    priceTBuyDic['CloseDay98'] = curStock.dayPriceClosedArray[matchDateIndex]*0.98
    priceTBuyDic['Lowest5'] = curStock.dayPriceLowestArray[matchDateIndex-5:matchDateIndex].min()
    priceTBuyDic['Lowest3'] = curStock.dayPriceLowestArray[matchDateIndex-3:matchDateIndex].min()
    for key,value in sorted(priceTBuyDic.items(), key=lambda x:-x[1]):
        print key,"\t",round(value,2)
   
##  �������Ʊ������ϣ��ж�ԭ�� MACD RSI 

##  ���ɵ�1.5���ϣ���T�ļ���һ����

if __name__=="__main__":
    startClock=time.clock() ##��¼����ʼ����ʱ��
    print ("�ϸ��ִ��ֹ�𷽰���")
    curStock=Stock('002285')
    calTBuy(curStock)
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
