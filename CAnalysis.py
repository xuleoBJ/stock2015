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
    
    
    stockID="601318"
    curStock=Cstock.Stock(stockID)
   
    
    numTradeDay=200
    print("�������"+str(numTradeDay)+"������:"+ curStock.dayStrList[-numTradeDay]+"-" +curStock.dayStrList[-1])
    
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
    print("����������3�콻���ո���"+str(numdays)+"���θ�����������"+str(up)+"���µ�����"+str(down))

## �������ǽ����գ��������Ǹ���
    for i in range(-numTradeDay,-1):
        if curStock.priceCloseingFList[i]>=curStock.priceCloseingFList[i-1]>=curStock.priceCloseingFList[i-2] \
                and curStock.dayTradeVolumeFList[i]<=curStock.dayTradeVolumeFList[i-1]<=curStock.dayTradeVolumeFList[i-2]:
                numdays=numdays+1
                if curStock.priceCloseingFList[i+1]>curStock.priceCloseingFList[i]:
                    up=up+1
                else:
                    down=down+1
    print("��������3���������ҽ������µ�"+str(numdays)+"���θ�����������"+str(up)+"���µ�����"+str(down))

## �������Ƿ��ȣ��������Ǹ���
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
        print("��������"+str(scale)+"%�����ո���"+str(numdays)+"���θ�����������"+str(up)+"���µ�����"+str(down))
   
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
        print("��������"+str(scale)+"%�����ո���"+str(numdays)+"���θ�����������"+str(up)+"���µ�����"+str(down))

## ������߼������̼۵ķ���
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
        print("��߼������̼۷��Ȳ�"+str(scale)+"~"+str(scale+1)+"%�����ո���"+str(numdays)+"���θ�����������"+str(up)+"���µ�����"+str(down))

## ������ͼ������̼۵ķ���
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
        print("��ͼ������̼۷��Ȳ�"+str(scale)+"~"+str(scale+1)+"%�����ո���"+str(numdays)+"���θ�����������"+str(up)+"���µ�����"+str(down))
   

    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


