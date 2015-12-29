# -*- coding: utf-8 -*-  
import os
import shutil
import time
import datetime
import sys
import Cstock
import Ccomfunc
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter  

lineWrited=[]

##�����Ƿ����ڶ������Ʒ���
##fList����Ҫ����������list�������Ƿ������߸߿����ݣ�flow���������������ֵ��fHigh���������������ֵ
def countTrendByRiseRate(cStock,fList,fLow,fHigh):
    fSelectList=[] 
    for k in range(0,len(cStock.dayRiseRateFList)-1):
        if fLow<=cStock.dayRiseRateFList[k]<=fHigh:
            fSelectList.append(fList[k+1])
    print("��������������{},>0�ĸ���{}".format(len(fSelectList),len(filter(lambda x:x>0,fSelectList))))

def volumeCompare():
    curStock=Stock('399001')
    shStock=Stock('999999')
    print ("���ܶԱȷ������5�����������ܶԱȣ�")
    print shStock.stockID,shStock.stockName,shStock.dayStrList[-5:],shStock.dayRadioLinkOfTradeVolumeFList[-5:]
    print curStock.stockID,curStock.stockName,curStock.dayStrList[-5:],curStock.dayRadioLinkOfTradeVolumeFList[-5:]

##���ݵ�һ������ƣ��ڶ������Ʒ���
##fList����Ҫ����������list�������Ƿ������߸߿����ݣ�flow���������������ֵ��fHigh���������������ֵ
def countTrendByOpenCloseRate(cStock,fList,fLow,fHigh):
    fSelectList=[] 
    for k in range(0,len(cStock.dayOpenCloseRateFList)-1):
        if fLow<=cStock.dayRiseRateFList[k]<=fHigh:
            fSelectList.append(fList[k+1])
    print("��������������{},>0�ĸ���{}".format(len(fSelectList),len(filter(lambda x:x>0,fSelectList))))

def trend(cStock):
    print ("��ȥ3��ͬ��20�����������ƣ�")
    today=datetime.date.today()
    for i in [1,2,3]:
        todayLastYear=today-datetime.timedelta(days=365*i) ##��׼ȷ���ǿ���
        print "{}��ͬ���Ƿ���".format(todayLastYear.year)
        for item in cStock.dateList:
            if todayLastYear-datetime.timedelta(days=1)<=item<=todayLastYear+datetime.timedelta(days=10):
                _index=cStock.dateList.index(item)
                print cStock.dayStrList[_index],cStock.dayRiseRateFList[_index]

##������Ʊ��������Ƶ�ͬ����
def analysisSynchronization(cStock,cMarketStock,dateStrStart,dateStrEnd):
## get analysis indexStartDay and indexEndDay by dayStrList
    indexStart=dayStrList.index(dateStrStart)
    indexEnd=dayStrList.index(dateStrEnd)
    print("-"*50)
    synFile=stockID+"syn.txt"
    fileWrited=open(synFile,'w')
    waveSHFList=[]
    waveStockFList=[]
## ͨ�������ҵ�����ͬ��index
    fileWrited.write("����"+"\t"+"�����Ƿ�"+"\t"+"��Ʊ�Ƿ�"+"\t"+ 'ͬ������\n')
    for i in range(indexStart,indexEnd):
        dateStrSH=dayStrList[i]
        indexSH=cMarketStock.index(dateStrSH)
        r1=round(100*(cStock.dayPriceClosedFList[i]-cStock.dayPriceClosedFList[i-1])/cStock.dayPriceClosedFList[i-1],2)
        waveStockFList.append(r1)
        rSH=round(100*(cMarketStock.dayPriceClosedFList[indexSH]-cMarketStock.dayPriceClosedFList[indexSH-1])/cMarketStock.dayPriceClosedFList[indexSH-1],2)
        waveSHFList.append(rSH)
        line=dateStrSH+"\t"+str(rSH)+"\t"+str(r1)+"\t"+ str(round(r1-rSH,2))
        fileWrited.write(line+'\n')
    fileWrited.close()
    print("��Ʊ�����ָ�����ϵ����"+str(pearsonr(waveSHFList,waveStockFList)))
    print("����ͬ���Է���д��"+synFile)


def compareStockAndMarket(cStock,strDateStart,strDateEnd):
    cMarketStock=Ccomfunc.getMarketStock(cStock.stockID) 
    dataDraw=[]
    indexOfStart=Ccomfunc.getIndexByStrdate(cStock,strDateStart)
    indexOfEnd=Ccomfunc.getIndexByStrdate(cStock,strDateEnd)
    ##�����Ƿ�
    rise= 100*(cStock.dayPriceClosedFList[indexOfEnd]-cStock.dayPriceClosedFList[indexOfStart-1])/cStock.dayPriceClosedFList[indexOfStart-1]
    dataDraw.append(rise)
    print "�Ƿ���{:.2f}".format(rise) 
    indexMax=indexOfStart+cStock.dayPriceHighestArray[indexOfStart:indexOfEnd].argmax()
    indexMin=indexOfStart+cStock.dayPriceHighestArray[indexOfStart:indexOfEnd].argmin()
    print "����͵�������ڣ�{}���ߵ����ڣ�{}".format(cStock.dayStrList[indexMin],cStock.dayStrList[indexMax])
    
    dateTick=range(iYearStart,iYearEnd)
    
    ind =np.arange(len(dateTick))    # the x locations for the groups
    width=0.35
    
    p1 = plt.bar(ind, dataDraw, width, color='r')
    plt.ylabel(u'riseRate')
    plt.title(cStock.stockID)
    ax=plt.gca()
    ymajorLocator = MultipleLocator(1) #��y�����̶ȱ�ǩ����Ϊ0.5�ı���
    ax.yaxis.set_major_locator(ymajorLocator)    
    plt.xticks(ind + width/2., dateTick)
    plt.show()

def statisticsRiselrate(cStock,iYearStart,iYearEnd,sMDStart,sMDEnd):## sMDStart="08/08"
     ##��ȥn��ͬ��ĳ��ʱ��ε��Ƿ�����ߵ���ֵ�ʱ�䣬��͵���ֵ�ʱ��
    dataDraw=[]
    print("##ͳ�Ʒ��������ͬ���������ڣ���ͬ�Ƿ��ĸ����ֲ�Ƶ��")
    for year in range(iYearStart,iYearEnd):
        headLine=str(year)+"��"+sMDStart+"-"+sMDEnd+"�ߵ�͵͵����ͳ�Ʒ�����"
        print(headLine)
        dateStrStart=str(year)+"/"+sMDStart
        indexOfStart=Ccomfunc.getIndexByStrDate(cStock,dateStrStart)
        dateStrEnd=str(year)+"/"+sMDEnd
        indexOfEnd=Ccomfunc.getIndexByStrDate(cStock,dateStrEnd)
        ##�����Ƿ�
        rise= 100*(cStock.dayPriceClosedFList[indexOfEnd]-cStock.dayPriceClosedFList[indexOfStart-1])/cStock.dayPriceClosedFList[indexOfStart-1]
        dataDraw.append(rise)
        print "�Ƿ���{:.2f}".format(rise) 
        indexMax=indexOfStart+cStock.dayPriceHighestArray[indexOfStart:indexOfEnd].argmax()
        indexMin=indexOfStart+cStock.dayPriceHighestArray[indexOfStart:indexOfEnd].argmin()
        print "����͵�������ڣ�{}���ߵ����ڣ�{}".format(cStock.dayStrList[indexMin],cStock.dayStrList[indexMax])
    
    dateTick=range(iYearStart,iYearEnd)
    
    ind =np.arange(len(dateTick))    # the x locations for the groups
    width=0.35
    
    barlist = plt.bar(ind, dataDraw, width, color='r')
    for i in range(len(dataDraw)):
        if dataDraw[i] <=0:
            barlist[i].set_color('g')
    plt.ylabel(u'riseRate')
    plt.title(cStock.stockID)
    ax=plt.gca()
    ymajorLocator = MultipleLocator(1) #��y�����̶ȱ�ǩ����Ϊ0.5�ı���
    ax.yaxis.set_major_locator(ymajorLocator)    
    plt.xticks(ind + width/2., dateTick)
    plt.show()

if __name__=="__main__":
   
    startClock=time.clock() ##��¼����ʼ����ʱ��

    stockID="002001"
    ##��ȡ��Ʊ���룬�洢��curStock��
    curStock=Cstock.Stock(stockID)
    curStock.list2array()
    curMarketStock=Ccomfunc.getMarketStock(stockID) 
    
    ##�Ƚ�����̵�ͬ����

    ##����ļ���
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    fileWrited.write(stockID+'\n')
    
    ##��ȥn��ͬ��ĳ��ʱ��ε��Ƿ�����ߵ���ֵ�ʱ�䣬��͵���ֵ�ʱ��
    print("##ͳ�Ʒ��������ͬ���������ڣ���ͬ�Ƿ��ĸ����ֲ�Ƶ��")
    iYearStart=2010
    iYearEnd=2015
    strDateStart="12/01"
    strDateEnd="12/31"
    dataDraw=statisticsRiselrate(curStock,iYearStart,iYearEnd,strDateStart,strDateEnd)
  
#    for year in range(2000,2015):
#        headLine=str(year)+"��12�¸ߵ�͵͵����ͳ�Ʒ�����"
#        print(headLine)
#        dateStrStart=str(year)+"/12/01"
#        indexOfStart=Ccomfunc.getIndexByStrdate(curStock,dateStrStart)
#        dateStrEnd=str(year)+"/12/31"
#        indexOfEnd=Ccomfunc.getIndexByStrdate(curStock,dateStrEnd)
#        ##�����Ƿ�
#        rise= 100*(curStock.dayPriceClosedFList[indexOfEnd]-curStock.dayPriceClosedFList[indexOfStart-1])/curStock.dayPriceClosedFList[indexOfStart-1]
#        dataDraw.append(rise)
#        print "�Ƿ���{:.2f}".format(rise) 
#        indexMax=indexOfStart+curStock.dayPriceHighestArray[indexOfStart:indexOfEnd].argmax()
#        indexMin=indexOfStart+curStock.dayPriceHighestArray[indexOfStart:indexOfEnd].argmin()
#        print "����͵�������ڣ�{}���ߵ����ڣ�{}".format(curStock.dayStrList[indexMin],curStock.dayStrList[indexMax])
#        fileWrited.write(headLine+"\n")

  
    
    ##���÷�������
    iDaysPeriodUser=len(curStock.dayStrList)
    ##��ʼ�������� dateStrStart
    dateStrStart=curStock.dayStrList[-iDaysPeriodUser]
    ##���˷������� dateStrEnd
    dateStrEnd=curStock.dayStrList[-1]
   
    ##����ʱ���ͳ�ƣ����������Ƶ�Ч��

    ##ͳ�Ʒ��������ͬ���������ڣ���ͬ�Ƿ��ĸ����ֲ�Ƶ��
    print("##ͳ�Ʒ��������ͬ���������ڣ���ͬ�Ƿ��ĸ����ֲ�Ƶ��")
    for dayPeriod in [300,150,90,60,30,20,10,5]:
        headLine=str(dayPeriod)+"����������ͳ�ƣ�\n�Ƿ��������:\t"
        print(headLine)
        fileWrited.write(headLine+"\n")
        for i in range(-10,11):
            _line=""
            _num=len(filter(lambda x:i==int(x),curStock.dayRiseRateFList[-dayPeriod:]))
            if i==10:
                _line="��ͣ��\t"+str(_num)
            else :
                _line=str(i)+"��"+str(i+1)+"\t"+str(_num)
            fileWrited.write(_line+'\n')
    
    ##������ͬ���������ڣ�ͳ�Ʋ�ͬ�������ȵĸ���Ƶ��
    print("##������ͬ���������ڣ�ͳ�Ʋ�ͬ�������ȵĸ���Ƶ��")
    for dayPeriod in [300,150,90,60,30,20,10,5]:
        headLine=str(dayPeriod)+"����������ͳ�ƣ�\n����������:\t"
        fileWrited.write(headLine+"\n")
        for i in range(0,21):
            _line=""
            _num=len(filter(lambda x:i==int(x),curStock.dayWaveRateFList[-dayPeriod:]))
            _line=str(i)+"��"+str(i+1)+"\t"+str(_num)
            fileWrited.write(_line+'\n')
    
    ##������ͬ���������ڣ�ͳ�ƿ��̸߿����Ϳ���Ƶ��
    print("##������ͬ���������ڣ�ͳ�ƿ��̸߿����Ϳ���Ƶ��")
    for dayPeriod in [30,20,10,5]:
        headLine=str(dayPeriod)+"����������ͳ�ƣ�\n���̵��Ƿ�Ƶ�ʷֲ�:\t"
        fileWrited.write(headLine+"\n")
        for i in range(-10,11):
            _line=""
            _num=len(filter(lambda x:i==int(x),curStock.dayOpenRateFList[-dayPeriod:]))
            _line=str(i)+"��"+str(i+1)+"\t"+str(_num)
            fileWrited.write(_line+'\n')
    
    print("##������ͬ���������ڣ�ͳ�����ֵ�뿪��ֵƵ�ʷֲ�")
    for dayPeriod in [300,150,90,60,30,20,10,5]:
        ##�������̼�����ͼ� �����������ռ۸�İٷֱȷֲ�
        ##������̼۾�����ͼۣ�������0��������̼۱���ͼ۲��󣬴����г��Ƚ�ǿ
        ##������̼�����ͼ۲��Ƚϴ󣬴���շ������Ƚϴ�
        headLine=str(dayPeriod)+"����������ͳ�ƣ�\n�������̼�����ͼ� �����������ռ۸�İٷֱ�Ƶ�ʷֲ�:\t \
        ##������̼۾�����ͼۣ�������0��������̼۱���ͼ۲��󣬴����г��Ƚ�ǿ  \
        ##������̼�����ͼ۲��Ƚϴ󣬴���շ������Ƚϴ� "
        fileWrited.write(headLine+"\n")
        for i in range(-20,1):
            _line=""
            _num=len(filter(lambda x:i==int(x),map(lambda x,y,z:100*(x-y)/z, \
                    curStock.dayPriceLowestFList[-dayPeriod:],curStock.dayPriceOpenFList[-dayPeriod:],curStock.dayPriceClosedFList[-dayPeriod-1:-1])))
            if i==0:
                _line="���̼۾�����ͼ�\t"+str(_num)
            else :
                _line=str(i)+"��"+str(i+1)+"\t"+str(_num)
            fileWrited.write(_line+'\n')

    ##������ͬ����������,�߿����ߣ��ڶ�����ǵ�
    for i in range(-10,11):
        print("��������{}%-{}%�������Ƿ��ֲ���".format(i,i+1))
        countTrendByOpenCloseRate(curStock,curStock.dayRiseRateFList,i-0.1,i+0.1)
  
    ##ͳ�Ʒ������̵�4����Ľ����յ����ƺʹ������ơ�
    
    ##ͳ�Ʒ��� ���ڴ��̿��̵�λ����͵�Ĳ��,���ֻ�ܽ�����Ч��������Ч
    ##���10�������յĸ����Ƕ���t��õĲο����ϡ�������ƾ�о�˵ ���ˣ����߸��ˣ�������
    ##�����߿����ߣ��Ϳ����ߣ��߿����ߣ��Ϳ����ߵĸ���
    ##�߿����������Ϳ�������
    
    ##�ɽ����䶯����
#    print ("���ڷ����ɽ����䶯��")
#    for i in range(-20,-1):
#        print curStock.dayStrList[i],curStock.dayRiseOfTradeVolumeFList[i],curStock.dayRiseOfTurnOverFList[i]
#    for i in range(-iDaysPeriodUser,-1):
#        ##��������������ʷͼ�У���һ�ܵ��������
#        if curStock.dayRiseRateFList[i-2]<=-3 and curStock.dayRiseRateFList[i]>=3 and curStock.dayPriceClosedFList[i-2]>curStock.dayPriceClosedFList[i-1]:
#            if curStock.dayWaveRateFList[i]>=3: ##���
#               if curStock.dayTradeVolumeFList[i-2]>curStock.dayTradeVolumeFList[i-1]>curStock.dayTradeVolumeFList[i]: ## �ɽ���
#                print(curStock.dayStrList[i])
#                fileWrited.write(curStock.dayStrList[i]+'\n')
#                 
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


