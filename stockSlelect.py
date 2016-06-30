# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Cstock
import Ccomfunc
import pdb
import trendAna
import numpy as np


##���ַ������stockIDList��selectScale=1 ���ı��ļ�stockIDList.txt ��ȡ =2����ѡ
def makeStockList(selectScale=0):
    stockIDList=["999999","399001"]
    ## �����ļ����ĵ�һ���ַ����ֹ�Ʊ���  ��֤6 ���� 0 ���ָ8 ��ҵ�� 3
    stockIDType=["8","3","6","0"]
    if selectScale == 1: ##��ѡ
        with open('stockIDList.txt') as fOpen:
            for line in fOpen:
                inner_list = [elt.strip() for elt in line.split(' ')]
                stockIDList.append(inner_list[0])
    if selectScale == 2 :  ##��ѡ
        fileNames=os.listdir(Ccomfunc.src)
        for fileItem in fileNames:
            if os.path.basename(fileItem)[0] in stockIDType: ## �����ļ����ĵ�һ���ַ����ֹ�Ʊ��� 
                stockIDList.append(os.path.splitext(fileItem)[0])
    return stockIDList

##��������ѡ���Ʊ
def selectStockByVolume():
    stockIDList=makeStockList()
    lineWritedList=[]
    
    shStock=Cstock.Stock("999999")
    sIDList = []  
    ##���� 1 �ž��� 2 ������������ 3 �������������µ�
    for stockID in stockIDList:
        curStock=Cstock.Stock(stockID)
        if curStock.count>0:  ##�޳�������Ϊ�յ� 
            ##3�������µ�
            if curStock.dayRadioLinkOfTradeVolumeArray[-1]<1 and curStock.dayRiseRateArray[-1]<0:
                if curStock.dayRadioLinkOfTradeVolumeArray[-2]<1 and curStock.dayRiseRateArray[-1]<0:
                    if curStock.dayRadioLinkOfTradeVolumeArray[-3]<1 and curStock.dayRiseRateArray[-1]<0:
                        sIDList.append(stockID)
                        sIDList.append("3")
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-3]))
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-2]))
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-1]))
            
            ##3�շ�������
            if curStock.dayRadioLinkOfTradeVolumeArray[-1]>1 and curStock.dayRiseRateArray[-1]>0:
                if curStock.dayRadioLinkOfTradeVolumeArray[-2]>1 and curStock.dayRiseRateArray[-1]>0:
                    if curStock.dayRadioLinkOfTradeVolumeArray[-3]>1 and curStock.dayRiseRateArray[-1]>0:
                        sIDList.append(stockID)
                        sIDList.append("2")
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-3]))
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-2]))
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-1]))

            ##�Ƚϴ��̺͸��ɵ�����ָ��ѡ���Ʊ,ѡ�������stockID
            if curStock.dayStrList[-1]==shStock.dayStrList[-1]:
                if curStock.dayRadioLinkOfTradeVolumeArray[-1]>=1.5:
                    if curStock.dayRadioLinkOfTradeVolumeArray[-1]-shStock.dayRadioLinkOfTradeVolumeArray[-1]>0.5:
                        sIDList.append(stockID)
                        sIDList.append("1")
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-3]))
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-2]))
                        sIDList.append(str(curStock.dayRadioLinkOfTradeVolumeArray[-1]))
            lineWritedList.append("\t".join(sIDList))
    print lineWritedList
    goalFilePath=os.path.join(Ccomfunc.resultDir,'_stockSelect.txt') ##����ļ���
    Ccomfunc.write2Text(goalFilePath,lineWritedList)

##����ѡ�ɵ�����
##1 ���Ƶķ�������
##2 Ŀ���λ��֧�ż�λ��

   
##����dateStr ������,interval �����ռ�����������������յ��Ƿ�
def selectStockByRiseRateBetween2Date(inputMDDateStart,inputMDDateEnd,yearList=[2015,2014,2013,2012,2011,2010],selectScale=2):
    stockIDList=makeStockList()
    lineWritedList=[]
    
    shStock=Cstock.Stock("999999")
    for stockID in stockIDList:
        ##��ȡ��Ʊ���룬�洢��curStock��
        curStock=Cstock.Stock(stockID)
        if curStock.count>0:
            sList = []
            sList.append(curStock.stockID)
            sList.append(curStock.stockName)
            riseList=[]
            riseSHList=[]
            iBig = 0 ##���������������Ƿ��Ա�
            for year in yearList:
                dateStrStart=str(year)+"/"+inputMDDateStart
                indexOfStartDate=Ccomfunc.getIndexByStrDate(curStock,dateStrStart)
                indexOfStartDateSH=Ccomfunc.getIndexByStrDate(shStock,dateStrStart)
                dateStrEnd=str(year)+"/"+inputMDDateEnd
                indexOfEndDate=Ccomfunc.getIndexByStrDate(curStock,dateStrEnd)
                indexOfEndDateSH=Ccomfunc.getIndexByStrDate(shStock,dateStrEnd)
                print indexOfStartDate,curStock.dayStrList[indexOfStartDate],indexOfEndDate,curStock.dayStrList[indexOfEndDate]
                if curStock.count>0 and indexOfStartDate>=0 and indexOfEndDate>0:
                    sList.append(curStock.dayStrList[indexOfStartDate])
                    sList.append(curStock.dayStrList[indexOfEndDate])
                    rise = -999
                    rise = trendAna.calRiseRateClosed(curStock,indexOfStartDate,indexOfEndDate)
                    riseList.append(rise)
                    riseSH = trendAna.calRiseRateClosed(shStock,indexOfStartDateSH,indexOfEndDateSH)
                    riseSHList.append(riseSH)
                    ##��¼ǿ�ڴ��̵ĸ���
                    if rise>=riseSH:
                        iBig = iBig+1
                    sList.append(str(round(rise,2)))
            sList.append(str(iBig))
            if stockID=="999999":
                sList.append(str(round(np.array(riseSHList).mean(),2)))
            else:
                sList.append(str(round(np.array(riseList).mean(),2)))

            lineWritedList.append("\t".join(sList))
    goalFilePath=os.path.join(Ccomfunc.resultDir,inputMDDateStart.replace("/","")+"-"+inputMDDateEnd.replace("/","")+'_stockSelect.txt') ##����ļ���
    Ccomfunc.write2Text(goalFilePath,lineWritedList)

## ����ָ��������Ƿ�ѡ��
def selectStockByMonthRise():
    stockIDList=makeStockList()
    
    print ("���ڸ�������ɸѡ��Ʊ��")
    ##�������ָ���¶����ݵ��Ƿ������й�Ʊ���ɸѡ����������������ѡ���һ����Ҫ����
    lineWritedList=[]
    strMonth="07"
    monthStrList=[ strMonth+ele for ele in ["2011","2012","2013","2014","2015"]]
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
    
    case=2
    ##����Ѱ���Ƿ�������У������Ƿ����ĸ���
    if case==1:
        selectStockByMonthRise() 
    if case==2:
        selectStockByRiseRateBetween2Date("06/01","06/15") 
        selectStockByRiseRateBetween2Date("06/16","06/30") 
        selectStockByRiseRateBetween2Date("07/01","07/15") 
        selectStockByRiseRateBetween2Date("07/16","07/30") 
    if case==3:
        selectStockByVolume()
   
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


