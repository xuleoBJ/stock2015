## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import numpy
import Cstock


##���㰴���ڼ�����ͣ����

lineWrited=[]

def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

def analysisScale(stockID,dateStrStart,dateStrEnd):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=dateStrList.index(dateStrStart)
    indexEnd=dateStrList.index(dateStrEnd)
    print("-"*50)
    print("�����۲���Ƿ�")
    
    zhenfuFList=[] ## ��������
    zhangdiefuFList=[]  ##�ǵ���
    for i in range(indexStart,indexEnd):
        priceDelta1=(priceCloseingFList[i]-priceOpeningFList[i])/priceCloseingFList[i-1]
        priceDelta2=(priceHighestFList[i]-priceLowestFList[i])/priceCloseingFList[i-1]
        if priceDelta1>=0.05:
            zhenfuFList.append(i)
        if abs(priceDelta2)>=0.05:
            zhangdiefuFList.append(i)
    strDate=""
    for item in zhenfuFList:
        strDate=strDate+dateStrList[item]+"\t"
    print("�������5%����:\t"+str(len(zhenfuFList))+"\t��ʼ�����ǣ�"+strDate)
    strDate=""
    for item in zhangdiefuFList:
        strDate=strDate+dateStrList[item]+"\t"
    print("�ǵ�������5%:\t"+str(len(zhangdiefuFList))+"\t��ʼ�����ǣ�"+strDate)

if __name__=="__main__":
    print("\n"+"#"*80)
    print ("�����з��գ�����������Ļ��ᣬ������Ҫ���ģ�����̬��Ҫ���档")
    print ("����������ƺ����������Ͳ��ȡ�")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##��¼����ʼ����ʱ��
   
    ##��ȡ��ָ֤������
    ##shStock=Cstock.StockSH()
    

    ##��ȡ��Ʊ���룬�洢��curStock��
    stockID="999999"
    curStock=Cstock.Stock(stockID)
    
    ##����ļ���
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    fileWrited.write(stockID+'\n')

    ##���÷�������
    iDaysPeriodUser=5000
    ##��ʼ�������� dateStrStart
    dateStrStart=curStock.dateStrList[-iDaysPeriodUser-1]
    ##���˷������� dateStrEnd
    dateStrEnd=curStock.dateStrList[-1]

    print ("���ڽ���ʱ�շ�����")
    for i in range(-iDaysPeriodUser,-1):
        ##��������������ʷͼ�У���һ�ܵ��������
        if  curStock.riseRateFList[i-3]>=2 and curStock.riseRateFList[i]<=-2:  ##
            if curStock.waveRateFList[i]>=3: ##���
 ##              if (curStock.tradeVolumeFList[i]-curStock.tradeVolumeFList[i-1])/curStock.tradeVolumeFList[i-1]>=0.1: ## �ɽ���
                print curStock.dateStrList[i]
                fileWrited.write(curStock.dateStrList[i]+'\n')
                 
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


