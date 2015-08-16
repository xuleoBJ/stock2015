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
    print ("����ʷK����Ѱ��������������Ϣ�����ڣ���Ϊ��ʷ���ظ��ģ�����Ҳ��ѭ���ġ�")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##��¼����ʼ����ʱ��
   

    stockIDList=[]
    sourceDirPath="export"
    fileNames=os.listdir(sourceDirPath)
    for fileItem in fileNames:
        stockIDList.append(os.path.splitext(fileItem)[0])
    
    ##����ļ���
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    
    print ("���ڸ�������ɸѡ��Ʊ��")
    
    for stockID in stockIDList:
        ##��ȡ��Ʊ���룬�洢��curStock��
        curStock=Cstock.Stock(stockID)
        if curStock.riseRateFList[-3]<= curStock.riseRateFList[-2]<=curStock.riseRateFList[-1]<0 and curStock.priceCloseingFList[-3]>curStock.priceCloseingFList[-2]>curStock.priceCloseingFList[-1]:
               if curStock.tradeVolumeFList[-3]>curStock.tradeVolumeFList[i-2]>curStock.tradeVolumeFList[-1]: ## �ɽ���
                print(stockID)
                fileWrited.write(stockID+'\n')
    fileWrited.close()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


