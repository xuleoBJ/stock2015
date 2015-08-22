## -*- coding: GBK -*-  
# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime

##����Ŀ¼
dirData="C:\\new_dxzq_v6\\T0002\\export\\" 

##��ȡָ������List
class Stock:
    dateStrList=[]
    priceOpeningFList=[]
    priceClosedFList=[]
    priceHighestFList=[]
    priceLowestFList=[]
    tradeVolumeFList=[] ##�ɽ���
    turnOverFList=[]  ##�ɽ���  ע���е�����û�гɽ���� �ɽ��������͹ɳ�Ȩ������
    riseRateFList=[]  ##�۸��Ƿ�
    waveRateFList=[] ##�����Ƿ�
    riseOfTradeVolumeFList=[]  ##�ɽ����Ƿ�
    riseOfTurnOverFList=[]  ##�ɽ����Ƿ�
    def __init__(self,stockID):
        print("#"*80)
        stockDataFile=os.path.join(dirData,stockID+'.txt')
        if os.path.exists(stockDataFile):
            fileOpened=open(stockDataFile,'r')
            lineIndex=0
            for line in fileOpened.readlines():
                lineIndex=lineIndex+1
                splitLine=line.split()
                if lineIndex==1:
                    print(line)
                if line!="" and lineIndex>=3 and len(splitLine)>=5:
                    self.dateStrList.append(splitLine[0])
                    self.priceOpeningFList.append(float(splitLine[1]))
                    self.priceHighestFList.append(float(splitLine[2]))
                    self.priceLowestFList.append(float(splitLine[3]))
                    self.priceClosedFList.append(float(splitLine[4]))
                    self.tradeVolumeFList.append(float(splitLine[5]))
                    self.turnOverFList.append(float(splitLine[6]))
                    ##�����Ƿ������
                    if len(self.priceClosedFList)>=2 and self.priceClosedFList[-1]>0:
			##(��������-��������)/��һ������
                        self.riseRateFList.append(round(100*(self.priceClosedFList[-1]-self.priceClosedFList[-2])/self.priceClosedFList[-2],2))
			##(�������-�������)/��һ������
                        self.waveRateFList.append(round(100*(self.priceHighestFList[-1]-self.priceLowestFList[-1])/self.priceClosedFList[-2],2))
                    else:
                        self.riseRateFList.append(-999)
                        self.waveRateFList.append(-999)
                    ##����ɽ����Ƿ�
                    if len(self.tradeVolumeFList)>=2 and self.tradeVolumeFList[-1]>0:
                        self.riseOfTradeVolumeFList.append(round(100*(self.tradeVolumeFList[-1]-self.tradeVolumeFList[-2])/self.tradeVolumeFList[-2],2))
                    else:
                        self.riseOfTradeVolumeFList.append(-999)
                        
                    if len(self.turnOverFList)>=2 and self.turnOverFList[-1]>0:
                        self.riseOfTurnOverFList.append(round(100*(self.turnOverFList[-1]-self.turnOverFList[-2])/self.turnOverFList[-2],2))
                    else:
                        self.riseOfTurnOverFList.append(-999)
            fileOpened.close()
            print("���ݶ�ȡ���,���ݿ�ʼ�գ�\t"+self.dateStrList[0]+"\t���ݽ����գ�\t"+self.dateStrList[-1])
        else:
            print(stockID+"���ݲ�����")


class StockSH:   
    shLineList=[]
    shDateStrList=[]
    shPriceOpeningFList=[]
    shPriceCloseingFList=[]
    shPriceHighestFList=[]
    shPriceLowestFList=[]
    shTradeVolumeFList=[]
    shTurnoverFList=[]
    shRiseRateFList=[]  ##�Ƿ�
    shWaveRateFLst=[] ##�����Ƿ�
    def __init__(self):
        print("#"*80)
        print ("��ǰ��Ʊ����:"+"sh999999")
        stockDataFile=os.path.join("export",'999999.txt')
        fileOpened=open(stockDataFile,'r')
        lineIndex=0
        for line in fileOpened.readlines():
            lineIndex=lineIndex+1
            splitLine=line.split()
            if line!="" and lineIndex>=3 and len(splitLine)>=6:
                self.shLineList.append(line)
                self.shDateStrList.append(splitLine[0])
                self.shPriceOpeningFList.append(float(splitLine[1]))
                self.shPriceHighestFList.append(float(splitLine[2]))
                self.shPriceLowestFList.append(float(splitLine[3]))
                self.shPriceCloseingFList.append(float(splitLine[4]))
                self.shTradeVolumeFList.append(float(splitLine[5]))
                self.shTurnoverFList.append(float(splitLine[6]))
        fileOpened.close()
        print("��֤���ݶ�ȡ���,���ݿ�ʼ�գ�\t"+self.shDateStrList[0]+"���ݽ����գ�\t"+self.shDateStrList[-1])
if __name__=="__main__":
    print("\n"+"#"*80)
    print ("�����з��գ�����������Ļ��ᣬ������Ҫ���ģ�����̬��Ҫ���档")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##��¼����ʼ����ʱ��
    
    curStock=Stock('999999')
    print curStock.dateStrList[-10:]
    print curStock.priceClosedFList[-10:]
    print curStock.priceHighestFList[-10:]
    print curStock.priceLowestFList[-10:]
    print curStock.riseRateFList[-10:]
    print curStock.waveRateFList[-10:]
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


