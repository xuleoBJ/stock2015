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

def calTBuy(curStock,strDate=Ccomfunc.defaultDateInputStr()):
    lineWritedList=[]
    matchDateIndex = Ccomfunc.getIndexByStrDate(curStock,strDate)
    lineWritedList.append("���ڣ�{}�����̼�{}".format(curStock.dayStrList[matchDateIndex],curStock.dayPriceClosedArray[matchDateIndex])) 
    priceTBuyDic={}
    priceTBuyDic['CloseYesto'] = curStock.dayPriceClosedArray[matchDateIndex]
    priceTBuyDic['CloseDay5Ave'] = curStock.day5PriceAverageArray[matchDateIndex]
    priceTBuyDic['CloseDay98'] = curStock.dayPriceClosedArray[matchDateIndex]*0.98
    priceTBuyDic['Lowest5'] = curStock.dayPriceLowestArray[matchDateIndex-5:matchDateIndex].min()
    priceTBuyDic['Lowest3'] = curStock.dayPriceLowestArray[matchDateIndex-3:matchDateIndex].min()
    headLine="����(��)����\t�͵�\t�ߵ�\t��λ"
    lineWritedList.append(headLine) 
    for period in [5,10,20,60]:
        cycleHigh=curStock.dayPriceHighestArray[matchDateIndex-period:matchDateIndex].max()
        cycleLow=curStock.dayPriceLowestArray[matchDateIndex-period:matchDateIndex].min()
        for keyPoint in [0.33,0.5,0.825]:
            resistLinePoint=cycleLow+(cycleHigh-cycleLow)*keyPoint
            resultLine="{}��\t{}\t{}\t{}\t{:.2f}".format(period,keyPoint,cycleLow,cycleHigh,resistLinePoint)
            if 0.99<=curStock.dayPriceClosedFList[matchDateIndex]/resistLinePoint<=1.01:
                if curStock.dayPriceClosedFList[matchDateIndex]<=resistLinePoint:
                    resultLine+="\tע��ѹ��λ��"
                if curStock.dayPriceClosedFList[matchDateIndex]>=resistLinePoint:
                    resultLine+="\t֧��λ��"
            lineWritedList.append(resultLine)
    for key,value in sorted(priceTBuyDic.items(), key=lambda x:-x[1]):
        line="{}\t{:.2f}".format(key,value)
        lineWritedList.append(line)
    for line in lineWritedList: 
        print line 
    goalFilePath=os.path.join(Ccomfunc.resultDir,curStock.stockID+"_"+strDate.replace("/","")+'_tradeTec.txt') ##����ļ���
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    os.startfile(goalFilePath)
    
##  �������Ʊ������ϣ��ж�ԭ�� MACD RSI 

##  ���ɵ�1.5���ϣ���T�ļ���һ����

if __name__=="__main__":
    startClock=time.clock() ##��¼����ʼ����ʱ��
    print ("�ϸ��ִ��ֹ�𷽰���")
    curStock=Stock('002001')
    calTBuy(curStock)
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
