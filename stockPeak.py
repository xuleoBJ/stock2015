# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import sys
import Cstock
import Ccomfunc
import trendAna


stockID="999999"

reload(sys)
sys.setdefaultencoding('utf-8')

##������ͬ���ڵĸߵ㼰����

def getDateOfPrice(price,priceFList,dayStrList):
    indexPrice=priceFList.index(price)
    return dayStrList[indexPrice]

def findPeakPrice(dayPeriod,curDateStrList,curPriceOpenFList,curPriceHighestFList,curPriceLowestFList,curPriceClosedFList):
    print('���м۸��ֵ��������������(��):'+str(dayPeriod))
    goalFilePath=os.path.join(resultDir,stockID+"_"+str(dayPeriod)+'_peakAnalysisPrice.txt') ##����ļ���
    lineWritedList=[]

    lineWritedList.append('-'*50)
    lineWritedList.append('�۸��ֵ������������(��):'+str(dayPeriod))
    lineWritedList.append("����"+"\t���ϴη�ֵ�����ո���\t"+"\t���ϴη�ֵ��Ȼ�ո���\t"+"\t�ֲ��ߵ�/�͵�\t"+"��������%:\t")
   
    ##���� ���ڼ��㽻���ռ��
    d1=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    standValue=100
    daySpanLast=10 ## record last span dayPeriod
    indexLast=1
    dayPeriod=dayPeriod/2 ##��������ֵ �ð�����ǰ���㣬iѭ��ʱ �Ƚϵ����Ƿ���ǰ������ڵļ�ֵ
    for i in range(dayPeriod,len(curDateStrList)):
        ##���iǰ���dayPeriod�������� ,i����Ľ����ղ���������� ����else��
        max_value = -999
        max_index = 0
        if i<len(curDateStrList)-dayPeriod:
            ##get the highest price of curStock in a period
            max_value = max(curPriceHighestFList[i-dayPeriod:i+dayPeriod])
            max_index = curPriceHighestFList.index(max_value)
        else:
            max_value = max(curPriceHighestFList[i-dayPeriod:])
            max_index = curPriceHighestFList.index(max_value)
            ## write to  file when  the max_index equals to i or pass 
        if max_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            daySpanLast=dayPeriod if daySpanLast==0 else daySpanLast
            riseRate=-999
            if standValue!=0:
                riseRate=round((max_value-standValue)/standValue,3)*100
            lineWritedList.append(curDateStrList[i]+"\t"+str(max_index-indexLast)+"\t"+str(daysSpan)+"\t" \
                    +str(curPriceHighestFList[i])+"\t"+str(riseRate)+"\t")
            d1=d2
            indexLast=max_index
            standValue=max_value
            daySpanLast=daysSpan
           
        min_value = 999 
        min_index = 0
        if i<len(curDateStrList)-dayPeriod:
            min_value = min(curPriceLowestFList[i-dayPeriod:i+dayPeriod])
            min_index = curPriceLowestFList.index(min_value)
        else:
            min_value = min(curPriceLowestFList[i-dayPeriod:])
            min_index = curPriceLowestFList.index(min_value)
        if min_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            riseRate=-999
            if standValue!=0:
                riseRate=round((min_value-standValue)/standValue,3)*100
            lineWritedList.append(curDateStrList[i]+"\t"+str(min_index-indexLast)+"\t"+str(daysSpan)+"\t" \
                    +str(curPriceLowestFList[i])+"\t"+str(riseRate)+"\t")
            d1=d2
            indexLast=min_index
            standValue=min_value
            daySpanLast=daysSpan
    ## deal the last day
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[-1])
    daysSpan=(d2-d1).days
    daySpanLast=dayPeriod if daySpanLast==0 else daySpanLast
    lineWritedList.append(curDateStrList[-1]+"\t" +str(len(curDateStrList)-indexLast)+"\t"+str(daysSpan)+"\t" \
            +str(curPriceClosedFList[-1])+"\t"+str(round((curPriceClosedFList[-1]-standValue)/standValue,3)*100))
    Ccomfunc.write2Text(goalFilePath,lineWritedList) 

def findPeakVolume(dayPeriod,curDateStrList,curTradeVolumeFList):
    print('���гɽ�����ֵ��������������(��):'+str(dayPeriod))
    goalFilePath=os.path.join(resultDir,stockID+"_"+str(dayPeriod)+'_peakAnalysisVolume.txt') ##����ļ���
    lineWritedList=[]
    lineWritedList.append('-'*50)
    lineWritedList.append('�ɽ�����ֵ��������(��):'+str(dayPeriod))
    lineWritedList.append("����"+"\t�ֲ��ߵ�/�͵�(����)\t"+"\t���ϴη�ֵ�����ո���\t"+"\t���ϴη�ֵ��Ȼ�ո���\t"+"\t��������%:\t")

    d1=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    standValue=100
    indexLast=1
    dayPeriod=dayPeriod/2
    for i in range(dayPeriod,len(curDateStrList)-dayPeriod):
        max_value = max(curTradeVolumeFList[i-dayPeriod:i+dayPeriod])
        max_index = curTradeVolumeFList.index(max_value)
        if max_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWritedList.append(curDateStrList[i]+"\t"+str(curTradeVolumeFList[i])+"\t"+str(max_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((max_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=max_index
            standValue=max_value
           
        min_value = min(curTradeVolumeFList[i-dayPeriod:i+dayPeriod])
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
    Ccomfunc.write2Text(goalFilePath,lineWritedList) 

def findPeakTurnover(dayPeriod,curDateStrList,curTurnover):
    print('���н��׶��ֵ��������������(��):'+str(dayPeriod))
    lineWritedList.append('-'*50)
    lineWritedList.append('�н��׶��ֵ��������(��):'+str(dayPeriod))
    lineWritedList.append("����"+"\t�ֲ��ߵ�/�͵�(��Ԫ)\t"+"\t���ϴη�ֵ�����ո���\t"+"\t���ϴη�ֵ��Ȼ�ո���\t"+"\t��������%:\t")
    d1=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    d2=Ccomfunc.convertDateStr2Date(curDateStrList[0])
    standValue=100
    indexLast=1
    dayPeriod=dayPeriod/2
    for i in range(dayPeriod,len(curDateStrList)-dayPeriod):
        max_value = max(curTurnover[i-dayPeriod:i+dayPeriod])
        max_index = curTurnover.index(max_value)
        if max_index==i:
            d2=Ccomfunc.convertDateStr2Date(curDateStrList[i])
            daysSpan=(d2-d1).days
            lineWritedList.append(curDateStrList[i]+"\t"+str(round(curTurnover[i]/10000,1))+"\t"+str(max_index-indexLast)+"\t"+str(daysSpan)+"\t"+str(round((max_value-standValue)/standValue,3)*100))
            d1=d2
            indexLast=max_index
            standValue=max_value
           
        min_value = min(curTurnover[i-dayPeriod:i+dayPeriod])
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

def analysisDate(dateStrStart,dateStrEnd,curDateStrList,curPriceOpenFList,curPriceHighestFList,curPriceLowestFList,curPriceClosedFList):
## get analysis indexStartDay and indexEndDay by dayStrList
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
## get analysis indexStartDay and indexEndDay by dayStrList
    indexStart=dayStrList.index(dateStrStart)
    indexEnd=dayStrList.index(dateStrEnd)
    print("-"*50)
    print("�����۲���Ƿ�")
    
    zhenfuFList=[] ## ��������
    zhangdiefuFList=[]  ##�ǵ���
    for i in range(indexStart,indexEnd):
        priceDelta1=(dayPriceClosedFList[i]-dayPriceOpenFList[i])/dayPriceClosedFList[i-1]
        priceDelta2=(dayPriceHighestFList[i]-dayPriceLowestFList[i])/dayPriceClosedFList[i-1]
        if priceDelta1>=0.05:
            zhenfuFList.append(i)
        if abs(priceDelta2)>=0.05:
            zhangdiefuFList.append(i)
    strDate=""
    for item in zhenfuFList:
        strDate=strDate+dayStrList[item]+"\t"
    print("�������5%����:\t"+str(len(zhenfuFList))+"\t��ʼ�����ǣ�"+strDate)
    strDate=""
    for item in zhangdiefuFList:
        strDate=strDate+dayStrList[item]+"\t"
    print("�ǵ�������5%:\t"+str(len(zhangdiefuFList))+"\t��ʼ�����ǣ�"+strDate)



if __name__=="__main__":
   
    startClock=time.clock() ##��¼����ʼ����ʱ��
    
    ##��ȡ��Ʊ���룬�洢��curStock��
    curStock=Cstock.Stock(stockID)

    ##���÷�������,������ڴ���1000��4���ȡ1000��������ȡ���
    iDaysPeriodUser=len(curStock.dayStrList) if len(curStock.dayStrList)<=1000 else 1000
    ##��ʼ�������� dateStrStart
    dateStrStart=curStock.dayStrList[-iDaysPeriodUser]
    ##���˷������� dateStrEnd
    dateStrEnd=curStock.dayStrList[-1]

    print ("���ڽ�����ʷʱ�շ�����")
    for dayPeriod in [3,5,10,20,30,60,90,120,250]:
        resultDir="resultDir"
        if not os.path.exists(resultDir):
            os.makedirs(resultDir)
       
        findPeakPrice(dayPeriod,curStock.dayStrList,curStock.dayPriceOpenFList,curStock.dayPriceHighestFList,curStock.dayPriceLowestFList,curStock.dayPriceClosedFList)
#        findPeakVolume(dayPeriod,curStock.dayStrList,curStock.dayTradeVolumeFList)
#        findPeakTurnover(dayPeriod,curStock.dayStrList,curStock.dayTurnOverFList)
        
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


