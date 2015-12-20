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
   
##  �������Ʊ������ϣ��ж�ԭ�� MACD RSI 

##  ���ɵ�1.5���ϣ���T�ļ���һ����

if __name__=="__main__":
    startClock=time.clock() ##��¼����ʼ����ʱ��
    print ("�ϸ��ִ��ֹ�𷽰���")
    curStock=Stock('002285')
    calTBuy(curStock)
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
