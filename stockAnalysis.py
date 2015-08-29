# -*- coding: utf-8 -*-
import os
import numpy as np
import shutil
import time
import datetime
import Cstock
import Ccomfunc

##���㰴���ڼ�����ͣ����

lineWrited=[]

def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

if __name__=="__main__":
    Ccomfunc.printInfor()
    
    startClock=time.clock() ##��¼����ʼ����ʱ��

    ##��ȡ��Ʊ���룬�洢��curStock��
    stockID="002673"
    curStock=Cstock.Stock(stockID)


    
    ##����ļ���
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    fileWrited.write(stockID+'\n')

    ##���÷�������
    iDaysPeriodUser=len(curStock.dateStrList)
    ##��ʼ�������� dateStrStart
    dateStrStart=curStock.dateStrList[-iDaysPeriodUser]
    ##���˷������� dateStrEnd
    dateStrEnd=curStock.dateStrList[-1]
    for days in [300,150,90,60,30,20,10,5]:
        headLine=str(days)+"����������ͳ�ƣ�\n�Ƿ��������:\t"
        print(headLine)
        fileWrited.write(headLine)
        for i in range(-10,11):
            _line=""
            _num=len(filter(lambda x:i<=x<i+1,curStock.riseRateFList[-days:]))
            if i==10:
                _line="��ͣ��\t"+str(_num)
            else :
                _line=str(i)+"��"+str(i+1)+"\t"+str(_num)
            print _line
            fileWrited.write(_line+'\n')
    ##�����������ǵ�Ƶ�ʲ���ֱ��ͼ
    ##�����߿����ߣ��Ϳ����ߣ��߿����ߣ��Ϳ����ߵĸ���
    ##����ÿ������ķ��ȷֲ�����ͼ
    ##��ͣ���ߵ�ͣ���ֵĸ���
    ##�߿����������Ϳ�������
    ##���÷�������
    ##�ɽ����䶯����
#    print ("���ڷ����ɽ����䶯��")
#    for i in range(-20,-1):
#        print curStock.dateStrList[i],curStock.riseOfTradeVolumeFList[i],curStock.riseOfTurnOverFList[i]
#    for i in range(-iDaysPeriodUser,-1):
#        ##��������������ʷͼ�У���һ�ܵ��������
#        if curStock.riseRateFList[i-2]<=-3 and curStock.riseRateFList[i]>=3 and curStock.priceClosedFList[i-2]>curStock.priceClosedFList[i-1]:
#            if curStock.waveRateFList[i]>=3: ##���
#               if curStock.tradeVolumeFList[i-2]>curStock.tradeVolumeFList[i-1]>curStock.tradeVolumeFList[i]: ## �ɽ���
#                print(curStock.dateStrList[i])
#                fileWrited.write(curStock.dateStrList[i]+'\n')
#                 
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


