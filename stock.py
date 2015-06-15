## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import numpy
from scipy.stats.stats import pearsonr


##������֤����ָ��List
shLineList=[]
shDateStrList=[]
shPriceOpeningFList=[]
shPriceCloseingFList=[]
shPriceHighestFList=[]
shPriceLowestFList=[]
shTradeVolumeFList=[]
shRiseRateFList=[]  ##�Ƿ�
shWaveRateFLst=[] ##�����Ƿ�

def readStockSH999999():
    print("\n"+"#"*80)
    print ("��ǰ��Ʊ����:"+"sh999999")
    stockDataFile=os.path.join(dataPath,'999999.txt')
    fileOpened=open(stockDataFile,'r')
    lineIndex=0
    for line in fileOpened.readlines():
        lineIndex=lineIndex+1
        splitLine=line.split()
        if line!="" and lineIndex>=3 and len(splitLine)>=6:
            shLineList.append(line)
            shDateStrList.append(splitLine[0])
            shPriceOpeningFList.append(float(splitLine[1]))
            shPriceHighestFList.append(float(splitLine[2]))
            shPriceLowestFList.append(float(splitLine[3]))
            shPriceCloseingFList.append(float(splitLine[4]))
            shTradeVolumeFList.append(float(splitLine[5]))
    fileOpened.close()
    print("��֤���ݶ�ȡ���,���ݿ�ʼ�գ�\t"+shDateStrList[0]+"���ݽ����գ�\t"+shDateStrList[-1])



##��ȡָ������List
lineList=[]
dateStrList=[]
priceOpeningFList=[]
priceCloseingFList=[]
priceHighestFList=[]
priceLowestFList=[]
tradeVolumeFList=[] ##�ɽ���
turnoverFList=[]  ##�ɽ���
riseRateFList=[]  ##�Ƿ�
waveRateFList=[] ##�����Ƿ�

def readStockByID(stockID):
    dirData="export"
    print("\n"+"#"*80)
    stockDataFile=os.path.join(dirData,stockID+'.txt')
##    if stockID.startswith("6"):
##        stockDataFile=os.path.join(dirData,"SH#"+stockID+'.txt')
##    else:
##        stockDataFile=os.path.join(dirData,"SZ#"+stockID+'.txt')
    fileOpened=open(stockDataFile,'r')
    lineIndex=0
    for line in fileOpened.readlines():
        lineIndex=lineIndex+1
        splitLine=line.split()
        if lineIndex==1:
            print(line)
        if line!="" and lineIndex>=3 and len(splitLine)>=5:
            lineList.append(line)
            dateStrList.append(splitLine[0])
            priceOpeningFList.append(float(splitLine[1]))
            priceHighestFList.append(float(splitLine[2]))
            priceLowestFList.append(float(splitLine[3]))
            priceCloseingFList.append(float(splitLine[4]))
            tradeVolumeFList.append(float(splitLine[5]))
            if len(priceCloseingFList)>=2:
                riseRateFList.append(round(100*(priceCloseingFList[-1]-priceCloseingFList[-2])/priceCloseingFList[-1],2))
                waveRateFList.append(round(100*(priceHighestFList[-1]-priceLowestFList[-2])/priceCloseingFList[-1],2))
            else:
                riseRateFList.append(0)
                waveRateFList.append(0)
    fileOpened.close()
    print("���ݶ�ȡ���,���ݿ�ʼ�գ�\t"+dateStrList[0]+"\t���ݽ����գ�\t"+dateStrList[-1])


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


###���������շ���###
def analysisConsecutive(stockID,dateStrStart,dateStrEnd,numConsecutiveTradeDays,fScale):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=dateStrList.index(dateStrStart)
    indexEnd=dateStrList.index(dateStrEnd)
    print("-"*50)
    print("����"+str(numConsecutiveTradeDays)+"�������շ��ȳ���"+str(fScale))
    
    waveFList=[] ## ��������
    for i in range(indexStart,indexEnd):
        priceDelta1=(priceCloseingFList[i-numConsecutiveTradeDays]-priceCloseingFList[i])/priceCloseingFList[i-numConsecutiveTradeDays]
        if abs(priceDelta1)>=fScale:
            waveFList.append(i)
    strDate=""
    for item in waveFList:
        strDate=strDate+dateStrList[item]+"\t"
    print("���������������:\t"+str(len(waveFList))+"\t��ʼ�����ǣ�"+strDate)

##������Ʊ��������Ƶ�ͬ����
def analysisSynchronization(stockID,dateStrStart,dateStrEnd):
## get analysis indexStartDay and indexEndDay by dateStrList
    indexStart=dateStrList.index(dateStrStart)
    indexEnd=dateStrList.index(dateStrEnd)
    print("-"*50)
    synFile=stockID+"syn.txt"
    fileWrited=open(synFile,'w')
    waveSHFList=[]
    waveStockFList=[]
## ͨ�������ҵ�����ͬ��index
    fileWrited.write("����"+"\t"+"�����Ƿ�"+"\t"+"��Ʊ�Ƿ�"+"\t"+ 'ͬ������\n')
    for i in range(indexStart,indexEnd):
        dateStrSH=dateStrList[i]
        indexSH=shDateStrList.index(dateStrSH)
        r1=round(100*(priceCloseingFList[i]-priceCloseingFList[i-1])/priceCloseingFList[i-1],2)
        waveStockFList.append(r1)
        rSH=round(100*(shPriceCloseingFList[indexSH]-shPriceCloseingFList[indexSH-1])/shPriceCloseingFList[indexSH-1],2)
        waveSHFList.append(rSH)
        line=dateStrSH+"\t"+str(rSH)+"\t"+str(r1)+"\t"+ str(round(r1-rSH,2))
        fileWrited.write(line+'\n')
    fileWrited.close()
    print("��Ʊ�����ָ�����ϵ����"+str(pearsonr(waveSHFList,waveStockFList)))
    print("����ͬ���Է���д��"+synFile)
    

if __name__=="__main__":
    print("\n"+"#"*80)
    print ("�����з��գ�����������Ļ��ᣬ������Ҫ���ģ�����̬��Ҫ���档")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##��¼����ʼ����ʱ��
    
    goalFilePath='result.txt'

    dataPath=u"Market" ##����ָ������Ŀ¼

    iDaysPeriodUser=300
    readStockSH999999()
    dateStrStart=shDateStrList[-iDaysPeriodUser-1]
    dateStrEnd=shDateStrList[-1]
    analysisDate(dateStrStart,dateStrEnd,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    print ("���ڽ��д���ʱ�շ�����")
    findPeak(30,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    findPeak(60,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    findPeak(90,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    findPeak(120,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    findPeak(180,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    findPeak(240,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)
    findPeak(300,shDateStrList,shPriceOpeningFList,shPriceHighestFList,shPriceLowestFList,shPriceCloseingFList)

    stockID="601766"
    readStockByID(stockID)

  ##  highAndlowPrice(stockID,[iDaysPeriodUser,30,60,120])
    for item in [iDaysPeriodUser,30,60,120]:
        dateStrStart=dateStrList[-item-1]
        dateStrEnd=dateStrList[-1]
        print("\n"+"$"*80)
        analysisDate(dateStrStart,dateStrEnd,dateStrList,priceOpeningFList,priceHighestFList,priceLowestFList,priceCloseingFList)
        ##�������������յĲ������Ⱥ���
        analysisScale(stockID,dateStrStart,dateStrEnd)
        numConsecutiveTradeDays=5
        fScale=0.1
        ##�������������յļ۲�
        analysisConsecutive(stockID,dateStrStart,dateStrEnd,numConsecutiveTradeDays,fScale)
    
    print ("���ڽ���ʱ�շ�����")
    findPeak(30,dateStrList,priceOpeningFList,priceHighestFList,priceLowestFList,priceCloseingFList)
    findPeak(60,dateStrList,priceOpeningFList,priceHighestFList,priceLowestFList,priceCloseingFList)
    findPeak(90,dateStrList,priceOpeningFList,priceHighestFList,priceLowestFList,priceCloseingFList)
    findPeak(120,dateStrList,priceOpeningFList,priceHighestFList,priceLowestFList,priceCloseingFList)
    findPeak(180,dateStrList,priceOpeningFList,priceHighestFList,priceLowestFList,priceCloseingFList)

    print ("�������������������")
    contiveTradeDaysAnalysis(5,dateStrList,riseRateFList)


    ##�����������ǽ����պ������µ������յĳɽ����Ա�

    fileWrited=open(goalFilePath,'w')
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    
    ##�����ͬ���Է���
    print("�����ͬ���Է���")
    numOfTradeDays=200
    analysisSynchronization(stockID,dateStrList[-numOfTradeDays],dateStrList[-1])


    print ("�����������ƣ�")
    numOfTradeDays=30
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
    raw_input()


