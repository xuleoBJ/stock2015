## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Cstock


##���㰴���ڼ�����ͣ����

lineWrited=[]

def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

if __name__=="__main__":
    print("\n"+"#"*80)
    print ("���Ʒ��գ��������ģ�̬�����档")
    print ("�µ�������Զ����Ʊ�����Ⱥ��������������β��15����������Ҫô�͹���Եĵͼ۵����㡣")
    print ("����ʷK����Ѱ�������Ƴɽ���������Ϣ�����ڣ���Ϊ��ʷ���ظ��ģ�����Ҳ��ѭ���ġ�")
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

    print ("���ڷ����ɽ����䶯��")
    for i in range(-20,-1):
        print curStock.dateStrList[i],curStock.riseOfTradeVolumeFList[i],curStock.riseOfTurnOverFList[i]
    for i in range(-iDaysPeriodUser,-1):
        ##��������������ʷͼ�У���һ�ܵ��������
        if curStock.riseRateFList[i-2]<=-3 and curStock.riseRateFList[i]>=3 and curStock.priceCloseingFList[i-2]>curStock.priceCloseingFList[i-1]:
 ##    if curStock.riseRateFList[i-2]<= curStock.riseRateFList[i-1]<=curStock.riseRateFList[i]<0 and curStock.priceCloseingFList[i-2]>curStock.priceCloseingFList[i-1]>curStock.priceCloseingFList[i]:
 ##       if  curStock.riseRateFList[i-3]>=2 and curStock.riseRateFList[i]<=-2:  ##
            if curStock.waveRateFList[i]>=3: ##���
               if curStock.tradeVolumeFList[i-2]>curStock.tradeVolumeFList[i-1]>curStock.tradeVolumeFList[i]: ## �ɽ���
                print(curStock.dateStrList[i])
                fileWrited.write(curStock.dateStrList[i]+'\n')
                 
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


