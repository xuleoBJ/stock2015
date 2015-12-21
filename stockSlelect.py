# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Cstock
import Ccomfunc
import pdb
import trendAna
##���㰴���ڼ�����ͣ����

##ѡƱ������

##�Ƚϸ����̵�����ѡƱ
def selectStockByVolume():
    stockIDList=["999999","399001"]
    fileNames=os.listdir(Ccomfunc.src)
    for fileItem in fileNames:
        ##������ͷѡ���ļ� ��֤6 ���� 0 ���ָ8 ��ҵ�� 3
        if os.path.basename(fileItem).startswith("6") or os.path.basename(fileItem).startswith("0") :
            stockIDList.append(os.path.splitext(fileItem)[0])
    lineWritedList=[]
    
    shStock=Cstock.Stock("999999")
    
    for stockID in stockIDList:
        curStock=Cstock.Stock(stockID)
        if curStock.dayStrList[-1]==shStock.dayStrList[-1]:
            if curStock.dayRadioLinkOfTradeVolumeArray[-1]>=1.5:
                if curStock.dayRadioLinkOfTradeVolumeArray[-1]-shStock.dayRadioLinkOfTradeVolumeArray[-1]>0.5:
                    print stockID
                    lineWritedList.append(stockID)
    print lineWritedList
    goalFilePath=os.path.join(Ccomfunc.resultDir,'_stockSelect.txt') ##����ļ���
    Ccomfunc.write2Text(goalFilePath,lineWritedList)

##����ѡ�ɵ�����
##1 ���Ƶķ�������
##2 Ŀ���λ��֧�ż�λ��

##����dateStr ������,interval �����ռ�����������������յ��Ƿ�
def selectStockByRiseRateBetween2Date(inputMDDateStart,inputMDDateEnd):
    stockIDList=["999999","399001"]
    fileNames=os.listdir(Ccomfunc.src)
    for fileItem in fileNames:
        ##������ͷѡ���ļ� ��֤6 ���� 0 ���ָ8 ��ҵ�� 3
        if os.path.basename(fileItem).startswith("6") or os.path.basename(fileItem).startswith("0") :
            stockIDList.append(os.path.splitext(fileItem)[0])
    lineWritedList=[]
    
    shStock=Cstock.Stock("999999")
    for stockID in stockIDList:
        ##��ȡ��Ʊ���룬�洢��curStock��
        curStock=Cstock.Stock(stockID)
        curStock.list2array()
        sList = []
        sList.append(curStock.stockID)
        sList.append(curStock.stockName)
        iBig = 0 ##���������������Ƿ��Ա�
        for year in [2010,2011,2012,2013,2014]:
            dateStrStart=str(year)+"/"+inputMDDateStart
            indexOfStartDate=Ccomfunc.getIndexByStrdate(curStock,dateStrStart)
            dateStrEnd=str(year)+"/"+inputMDDateEnd
            indexOfEndDate=Ccomfunc.getIndexByStrdate(curStock,dateStrEnd)
            sList.append(curStock.dayStrList[indexOfStartDate])
            sList.append(curStock.dayStrList[indexOfEndDate])
            rise = -999
    #        pdb.set_trace()
            if indexOfStartDate>=0:
                rise = trendAna.calRiseRate(curStock,indexOfStartDate,indexOfEndDate)
                riseSH = trendAna.calRiseRate(shStock,indexOfStartDate,indexOfEndDate)
                ##��¼ǿ�ڴ��̵ĸ���
                if rise>=riseSH:
                    iBig = iBig+1
            sList.append(str(round(rise,2)))
        sList.append(str(iBig))
        lineWritedList.append("\t".join(sList))
    goalFilePath=os.path.join(Ccomfunc.resultDir,'_stockSelect.txt') ##����ļ���
    Ccomfunc.write2Text(goalFilePath,lineWritedList)

## ����ָ��������Ƿ�ѡ��
def selectStockByMonthRise():
    stockIDList=[]
    if len(stockIDList)==0:
        fileNames=os.listdir(Ccomfunc.dirHisData)
        for fileItem in fileNames:
            ##������ͷѡ���ļ� ��֤6 ���� 0 ���ָ8 ��ҵ�� 3
            if os.path.basename(fileItem).startswith("8") or os.path.basename(fileItem).startswith("9") :
                stockIDList.append(os.path.splitext(fileItem)[0])
    
   
    print ("���ڸ�������ɸѡ��Ʊ��")
    ##�������ָ���¶����ݵ��Ƿ������й�Ʊ���ɸѡ����������������ѡ���һ����Ҫ����
    lineWritedList=[]
    monthStrList=["201112","201212","201312","201412"]
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
    goalFilePath='result.txt'
    Ccomfunc.write2Text(goalFilePath,lineWritedList)

if __name__=="__main__":
   
    startClock=time.clock() ##��¼����ʼ����ʱ��

   #lineWritedList=selectStockByMonthRise() 
    
   # lineWritedList=selectStockByRiseRateBetween2Date("12/20","12/31") 
    selectStockByVolume()
    ##����Ѱ���Ƿ�������У������Ƿ����ĸ���
    
    ##����Ѱ���Ƿ�������У�����3-5���������Ƿ����ĸ���
   
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


