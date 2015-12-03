# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Cstock
import Ccomfunc
import pdb
##���㰴���ڼ�����ͣ����

##ѡƱ������

##����ѡ�ɵ�����
##1 ���Ƶķ�������
##2 Ŀ���λ��֧�ż�λ��

##���������������ڣ��������������յ��Ƿ�
def calRiseRateBetween2Date(dateStr,interval):
    ##key is dateStr��ָ��Ѱ�ң��ǲ��ǽ����գ�����Ҳ�����ô�죿
    ##�ж�datestr�Ƿ������ݣ�
    ##���û�У�����+1�����жϣ���û����+1
    stockIDList=[]
    if len(stockIDList)==0:
        fileNames=os.listdir(Ccomfunc.dirHisData)
        for fileItem in fileNames:
            ##������ͷѡ���ļ� ��֤6 ���� 0 ���ָ8 ��ҵ�� 3
            if os.path.basename(fileItem).startswith("6") or os.path.basename(fileItem).startswith("0") :
                stockIDList.append(os.path.splitext(fileItem)[0])
    lineWritedList=[]
    
    for stockID in stockIDList:
        ##��ȡ��Ʊ���룬�洢��curStock��
        curStock=Cstock.Stock(stockID,Ccomfunc.dirHisData)
        curStock.list2array()
        indexOfDate=Ccomfunc.getIndexByStrdate(curStock,dateStr)
#        pdb.set_trace()

        ##������������ͣ�Ʊ��ǵ�ɾ���ˣ����� ȥ������Խ���
        if indexOfDate<0:
            pass
        elif len(curStock.dayStrList)<indexOfDate+interval:
            pass
        elif (curStock.dateList[indexOfDate+interval]-curStock.dateList[indexOfDate]).days>interval*2: ##������������ͣ�Ʊ��ǵ�ɾ����
            pass
        else:
            sList=[]
            sList.append(curStock.stockID)
            sList.append(curStock.stockName)
            sList.append(curStock.dayStrList[indexOfDate])
            sList.append(curStock.dayStrList[indexOfDate+interval])
            rise= 100*(curStock.dayPriceClosedFList[indexOfDate+interval]-curStock.dayPriceClosedFList[indexOfDate])/curStock.dayPriceClosedFList[indexOfDate]
            sList.append(str(round(rise,2)))
            lineWritedList.append("\t".join(sList))

    goalFilePath='_result.txt'
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
    
    lineWritedList=calRiseRateBetween2Date("2013/12/04",10) 
    
    ##����Ѱ���Ƿ�������У������Ƿ����ĸ���
    
    ##����Ѱ���Ƿ�������У�����3-5���������Ƿ����ĸ���
   
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


