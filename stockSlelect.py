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
    monthStrList=["201109","201209","201309","201409"]
    for stockID in stockIDList:
        ##��ȡ��Ʊ���룬�洢��curStock��
        curStock=Cstock.Stock(stockID)
        sList=[]
        sList.append(curStock.stockID)
        sList.append(curStock.stockName)
        for sMonth in monthStrList:
            sList.append(sMonth)
            _riseRateMonth="-999"
            for i in range(len(curStock.monthStrList)):
                if curStock.monthStrList[i].endswith(sMonth):
                    _riseRateMonth=str(curStock.monthRiseRateFList[i])
            sList.append(_riseRateMonth)
        lineWritedList.append("\t".join(sList))
    ##����ļ���
    goalFilePath='result.txt'
    Ccomfunc.write2Text(goalFilePath,lineWritedList)
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


