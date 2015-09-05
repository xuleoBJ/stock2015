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
    
    if len(stockIDList)==0:
        fileNames=os.listdir(Ccomfunc.dirData)
        for fileItem in fileNames:
            ##������ͷѡ���ļ� ��֤6 ���� 0 ���ָ8 ��ҵ�� 3
            if os.path.basename(fileItem).startswith("8"):
                stockIDList.append(os.path.splitext(fileItem)[0])
    
   
    print ("���ڸ�������ɸѡ��Ʊ��")
    ##�������ָ���¶����ݵ��Ƿ������й�Ʊ���ɸѡ����������������ѡ���һ����Ҫ����
    lineWritedList=[]
    for stockID in stockIDList:
        ##��ȡ��Ʊ���룬�洢��curStock��
        curStock=Cstock.Stock(stockID)
        sMonth="201212"
        for i in range(len(curStock.monthStrList)):
            if curStock.monthStrList[i].endswith(sMonth):
                lineWritedList.append(curStock.stockID+"\t"+curStock.stockName+"\t"+sMonth+"\t"+str(curStock.monthRiseRateFList[i]))
    ##����ļ���
    goalFilePath='result.txt'
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


