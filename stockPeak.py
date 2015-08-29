# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import sys
import Cstock
import Ccomfunc

reload(sys)
sys.setdefaultencoding('utf-8')

##���㰴���ڼ�����ͣ����

lineWritedList=[]

def getDateOfPrice(price,priceFList,dateStrList):
    indexPrice=priceFList.index(price)
    return dateStrList[indexPrice]


def findPeakPrice(days,curDateStrList,curPriceOpeningFList,curPriceHighestFList,curPriceLowestFList,curPriceCloseingFList):
    print('���м۸��ֵ��������������(��):'+str(days))
    lineWritedList.append('-'*50)
    lineWritedList.append('�۸��ֵ������������(��):'+str(days))
    lineWritedList.append("����"+"\t���ϴη�ֵ�����ո���\t"+"\t���ϴη�ֵ��Ȼ�ո���\t"+"\t��Ȼ�ռ������"+"\t�ֲ��ߵ�/�͵�\t"+"��������%:\t")
    ##
    d1=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    standValue=100
    daySpanLast=10 ## record last span days
    indexLast=1
    days=days/2
    for i in range(days,len(curDateStrList)-days):
##        index, value = max(enumerate(curPriceHighestFList[i-days:i+days]), key=operator.itemgetter(1))
        ##get the highest price of curStock in a period
        max_value = max(curPriceHighestFList[i-days:i+days])
        max_index = curPriceHighestFList.index(max_value)
        ## write to  file when  the max_index equals to i or pass 
        if max_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            daySpanLast=days if daySpanLast==0 else daySpanLast
            lineWritedList.append(curDateStrList[i]+"\t"+str(max_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round(daysSpan/float(daySpanLast),3))+"\t" \
                    +str(curPriceHighestFList[i])+"\t"+str(round((max_value-standValue)/standValue,3)*100)+"\t")
            d1=d2
            indexLast=max_index
            standValue=max_value
            daySpanLast=daysSpan
           
        min_value = min(curPriceLowestFList[i-days:i+days])
        min_index = curPriceLowestFList.index(min_value)
        if min_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWritedList.append(curDateStrList[i]+"\t"+str(min_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round(daysSpan/float(daySpanLast),3))+"\t" \
                    +str(curPriceLowestFList[i])+"\t"+str(round((min_value-standValue)/standValue,3)*100)+"\t")
            d1=d2
            indexLast=min_index
            standValue=min_value
            daySpanLast=daysSpan
    ## deal the last day
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[-1])
    daysSpan=(d2-d1).days
    daySpanLast=days if daySpanLast==0 else daySpanLast
    lineWritedList.append(curDateStrList[-1]+"\t" +str(len(curDateStrList)-indexLast)+"\t"+str(daysSpan)+"\t"+str(round(daysSpan/float(daySpanLast),3))+"\t" \
            +str(curPriceCloseingFList[-1])+"\t"+str(round((curPriceCloseingFList[-1]-standValue)/standValue,3)*100))

def findPeakVolume(days,curDateStrList,curTradeVolumeFList):
    print('���гɽ�����ֵ��������������(��):'+str(days))
    lineWritedList.append('-'*50)
    lineWritedList.append('�ɽ�����ֵ��������(��):'+str(days))
    lineWritedList.append("����"+"\t�ֲ��ߵ�/�͵�(����)\t"+"\t���ϴη�ֵ�����ո���\t"+"\t���ϴη�ֵ��Ȼ�ո���\t"+"\t��������%:\t")

    d1=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    standValue=100
    indexLast=1
    days=days/2
    for i in range(days,len(curDateStrList)-days):
        max_value = max(curTradeVolumeFList[i-days:i+days])
        max_index = curTradeVolumeFList.index(max_value)
        if max_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWritedList.append(curDateStrList[i]+"\t"+str(curTradeVolumeFList[i])+"\t"+str(max_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((max_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=max_index
            standValue=max_value
           
        min_value = min(curTradeVolumeFList[i-days:i+days])
        min_index = curTradeVolumeFList.index(min_value)
        if min_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWritedList.append(curDateStrList[i]+"\t"+str(curTradeVolumeFList[i])+"\t"+str(min_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((min_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=min_index
            standValue=min_value
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[-1])
    daysSpan=(d2-d1).days
    lineWritedList.append(curDateStrList[-1]+"\t"+str(curTradeVolumeFList[-1])+"\t"+str(len(curDateStrList)-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((curTradeVolumeFList[-1]-standValue)/standValue,3)*100))


def findPeakTurnover(days,curDateStrList,curTurnover):
    print('���н��׶��ֵ��������������(��):'+str(days))
    lineWritedList.append('-'*50)
    lineWritedList.append('�н��׶��ֵ��������(��):'+str(days))
    lineWritedList.append("����"+"\t�ֲ��ߵ�/�͵�(��Ԫ)\t"+"\t���ϴη�ֵ�����ո���\t"+"\t���ϴη�ֵ��Ȼ�ո���\t"+"\t��������%:\t")
    d1=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    standValue=100
    indexLast=1
    days=days/2
    for i in range(days,len(curDateStrList)-days):
        max_value = max(curTurnover[i-days:i+days])
        max_index = curTurnover.index(max_value)
        if max_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWritedList.append(curDateStrList[i]+"\t"+str(round(curTurnover[i]/10000,1))+"\t"+str(max_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((max_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=max_index
            standValue=max_value
           
        min_value = min(curTurnover[i-days:i+days])
        min_index = curTurnover.index(min_value)
        if min_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWritedList.append(curDateStrList[i]+"\t"+str(round(curTurnover[i]/10000,1))+"\t"+str(min_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((min_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=min_index
            standValue=min_value
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[-1])
    daysSpan=(d2-d1).days
    lineWritedList.append(curDateStrList[-1]+"\t"+str(round(curTurnover[-1]/10000,1))+"\t"+str(len(curDateStrList)-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((curTurnover[-1]-standValue)/standValue,3)*100))

def analysisDate(dateStrStart,dateStrEnd,curDateStrList,curPriceOpeningFList,curPriceHighestFList,curPriceLowestFList,curPriceCloseingFList):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=curDateStrList.index(dateStrStart)
    indexEnd=curDateStrList.index(dateStrEnd)
    print("-"*50)
    print("��������(������/��):\t"+str(indexEnd-indexStart)+"��ʼ����:\t"+curDateStrList[indexStart]+"\t��������:"+curDateStrList[indexEnd])
    
    curPriceHighest=max(curPriceHighestFList[indexStart:indexEnd])
    datePriceHighest=getDateOfPrice(curPriceHighest,curPriceHighestFList,curDateStrList)
    print("��������߼�:\t"+str(curPriceHighest)+"��������:\t"+datePriceHighest)
    
    curPriceLowest=min(curPriceLowestFList[indexStart:indexEnd])
    datePriceLowest=getDateOfPrice(curPriceLowest,curPriceLowestFList,curDateStrList)
    print("��������ͼ�:\t"+str(curPriceLowest)+"��������:\t"+datePriceLowest)

    natureDaysNumFromLastPeak2Today=-1  
    if datePriceHighest>=datePriceLowest:
        natureDaysNumFromLastPeak2Today=datetime.date.today()-Ccomfunc.convertDateStr2Date(datePriceHighest)
    else:
        natureDaysNumFromLastPeak2Today=datetime.date.today()-Ccomfunc.convertDateStr2Date(datePriceLowest)
    print("�ϸ���ֵ����������Ȼ�ո���(��):\t"+str(natureDaysNumFromLastPeak2Today.days))
    print("��ߵ��������͵���ֽ����ո���(��):\t"+str(1+curPriceHighestFList.index(curPriceHighest)-curPriceLowestFList.index(curPriceLowest)))
    daySpan=calNatureDays(datePriceHighest,datePriceLowest)
    print("��ߵ��������͵������Ȼ�ո���(��):\t"+str(daySpan))
    print("��ߵ�/��͵�:\t"+str(round(curPriceHighest/curPriceLowest,2)))

def analysisScale(stockID,dateStrStart,dateStrEnd):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=dateStrList.index(dateStrStart)
    indexEnd=dateStrList.index(dateStrEnd)
    print("-"*50)
    print("�����۲���Ƿ�")
    
    zhenfuFList=[] ## ��������
    zhangdiefuFList=[]  ##�ǵ���
    for i in range(indexStart,indexEnd):
        priceDelta1=(priceClosedFList[i]-priceOpeningFList[i])/priceClosedFList[i-1]
        priceDelta2=(priceHighestFList[i]-priceLowestFList[i])/priceClosedFList[i-1]
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
    

    ##���÷�������
    iDaysPeriodUser=800
    ##��ʼ�������� dateStrStart
    dateStrStart=curStock.dateStrList[-iDaysPeriodUser-1]
    ##���˷������� dateStrEnd
    dateStrEnd=curStock.dateStrList[-1]

    print ("���ڽ�����״������")
    for days in [3,5,10,20,30]:
	 Ccomfunc.printCalTrend(curStock,days)
	   

    print ("���ڽ�����ʷʱ�շ�����")
    for days in [5,10,20,30,60,90,120,180,300]:
        resultDir="resultDir"
        if not os.path.exists(resultDir):
            os.makedirs(resultDir)
        goalFilePath=os.path.join(resultDir,stockID+"_"+str(days)+'_��ֵ������ʷ����.txt') ##����ļ���
        lineWritedList=[]
        findPeakPrice(days,curStock.dateStrList,curStock.priceOpeningFList,curStock.priceHighestFList,curStock.priceLowestFList,curStock.priceClosedFList)
        findPeakVolume(days,curStock.dateStrList,curStock.tradeVolumeFList)
        findPeakTurnover(days,curStock.dateStrList,curStock.turnOverFList)
        fileWrited=open(goalFilePath,'w')
        fileWrited.write(stockID+'\n')
        for line in lineWritedList:
            fileWrited.write(line+'\n')
        fileWrited.close()
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


