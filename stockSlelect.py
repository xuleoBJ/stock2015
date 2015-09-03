# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Cstock
import Ccomfunc

##���㰴���ڼ�����ͣ����

lineWrited=[]

if __name__=="__main__":
   
    startClock=time.clock() ##��¼����ʼ����ʱ��
   

    stockIDList=[]
    
    fileNames=os.listdir(Ccomfunc.dirData)
    for fileItem in fileNames:
        ##������ͷѡ���ļ� ��֤6 ���� 0 ���ָ8 ��ҵ�� 3
        if os.path.basename(fileItem).startswith("8"):
            stockIDList.append(os.path.splitext(fileItem)[0])
    
    ##����ļ���
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    
    print ("���ڸ�������ɸѡ��Ʊ��")
    ##�������ָ���¶����ݵ��Ƿ������й�Ʊ���ɸѡ����������������ѡ���һ����Ҫ����

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


