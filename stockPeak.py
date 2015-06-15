## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import numpy
import Cstock


##���㰴���ڼ�����ͣ����

lineWrited=[]

def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

def calNatureDays(dateStr1,dateStr2):
    d1= convertDateStr2Date(dateStr1)
    d2= convertDateStr2Date(dateStr2)
    return (d1-d2).days

def getDateOfPrice(price,priceFList,dateStrList):
    indexPrice=priceFList.index(price)
    return dateStrList[indexPrice]


def findPeak(days,curDateStrList,curPriceOpeningFList,curPriceHighestFList,curPriceLowestFList,curPriceCloseingFList):
    print('���з�ֵ��������������(��):'+str(days))
    lineWrited.append('-'*50)
    lineWrited.append('��������(��):'+str(days))
    lineWrited.append("����"+"\t�ֲ��ߵ�/�͵�\t"+"\t���ϴη�ֵ�����ո���\t"+"\t���ϴη�ֵ��Ȼ�ո���\t"+"\t��������%:\t")
    d1=convertDateStr2Date(curDateStrList[0])
    d2=convertDateStr2Date(curDateStrList[0])
    standValue=100
    indexLast=1
    days=days/2
    for i in range(days,len(curDateStrList)-days):
##        index, value = max(enumerate(curPriceHighestFList[i-days:i+days]), key=operator.itemgetter(1))
        max_value = max(curPriceHighestFList[i-days:i+days])
        max_index = curPriceHighestFList.index(max_value)
        if max_index==i:
            d2=convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWrited.append(curDateStrList[i]+"\t"+str(curPriceHighestFList[i])+"\t"+str(max_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((max_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=max_index
            standValue=max_value
           
        min_value = min(curPriceLowestFList[i-days:i+days])
        min_index = curPriceLowestFList.index(min_value)
        if min_index==i:
            d2=convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWrited.append(curDateStrList[i]+"\t"+str(curPriceLowestFList[i])+"\t"+str(min_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((min_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=min_index
            standValue=min_value
    d2=convertDateStr2Date(curDateStrList[-1])
    daysSpan=(d2-d1).days
    lineWrited.append(curDateStrList[-1]+"\t"+str(curPriceCloseingFList[-1])+"\t"+str(len(curDateStrList)-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((curPriceCloseingFList[-1]-standValue)/standValue,3)*100))


def contiveTradeDaysAnalysis(numDays,curDateStrList,curRiseRateFList):
    lineWrited.append('-'*50)
    lineWrited.append('�����µ������ո���:'+str(numDays))
    indexList=[]
    for i in range(0,len(curRiseRateFList)-numDays):
        bFall=0
        for j in range(numDays):
            if curRiseRateFList[i+j]>=0:
                bFall=1
        if bFall==0:
            print curDateStrList[i]
  ##  lineWrited.append(curDateStrList[-1]+"\t"+str(curPriceCloseingFList[-1])+"\t"+str(len(curDateStrList)-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((curPriceCloseingFList[-1]-standValue)/standValue,3)*100))




def analysisDate(dateStrStart,dateStrEnd,curDateStrList,curPriceOpeningFList,curPriceHighestFList,curPriceLowestFList,curPriceCloseingFList):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=curDateStrList.index(dateStrStart)
    indexEnd=curDateStrList.index(dateStrEnd)
    print("-"*50)
    print("��������(������/��):\t"+str(indexEnd-indexStart)+"\t��ʼ����:"+curDateStrList[indexStart]+"\t��������:"+curDateStrList[indexEnd])
    
    curPriceHighest=max(curPriceHighestFList[indexStart:indexEnd])
    datePriceHighest=getDateOfPrice(curPriceHighest,curPriceHighestFList,curDateStrList)
    print("��������߼�:\t"+str(curPriceHighest)+"\t��������:\t"+datePriceHighest)
    
    curPriceLowest=min(curPriceLowestFList[indexStart:indexEnd])
    datePriceLowest=getDateOfPrice(curPriceLowest,curPriceLowestFList,curDateStrList)
    print("��������ͼ�:\t"+str(curPriceLowest)+"\t��������:\t"+datePriceLowest)

    natureDaysNumFromLastPeak2Today=-1  
    if datePriceHighest>=datePriceLowest:
        natureDaysNumFromLastPeak2Today=datetime.date.today()-convertDateStr2Date(datePriceHighest)
    else:
        natureDaysNumFromLastPeak2Today=datetime.date.today()-convertDateStr2Date(datePriceLowest)
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
        priceDelta1=(priceCloseingFList[i]-priceOpeningFList[i])/priceCloseingFList[i-1]
        priceDelta2=(priceHighestFList[i]-priceLowestFList[i])/priceCloseingFList[i-1]
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
    print("\n"+"#"*80)
    
    startClock=time.clock() ##��¼����ʼ����ʱ��
    
    shStock=Cstock.StockSH()
    
    stockID="601766"
    curStock=Cstock.Stock(stockID)
    
    goalFilePath='result.txt'

    iDaysPeriodUser=300
    dateStrStart=curStock.dateStrList[-iDaysPeriodUser-1]
    dateStrEnd=curStock.dateStrList[-1]

    print ("���ڽ���ʱ�շ�����")
    findPeak(30,curStock.dateStrList,curStock.priceOpeningFList,curStock.priceHighestFList,curStock.priceLowestFList,curStock.priceCloseingFList)
    findPeak(60,curStock.dateStrList,curStock.priceOpeningFList,curStock.priceHighestFList,curStock.priceLowestFList,curStock.priceCloseingFList)
    findPeak(90,curStock.dateStrList,curStock.priceOpeningFList,curStock.priceHighestFList,curStock.priceLowestFList,curStock.priceCloseingFList)
    findPeak(120,curStock.dateStrList,curStock.priceOpeningFList,curStock.priceHighestFList,curStock.priceLowestFList,curStock.priceCloseingFList)
    findPeak(180,curStock.dateStrList,curStock.priceOpeningFList,curStock.priceHighestFList,curStock.priceLowestFList,curStock.priceCloseingFList)


    fileWrited=open(goalFilePath,'w')
    fileWrited.write(stockID+'\n')
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
    raw_input()


