# -*- coding: utf-8 -*-
import os
import shutil
import time
import datetime
import Ccomfunc

##����Ŀ¼
dirData="C:\\new_dxzq_v6\\T0002\\export\\" 

##��ȡָ������List
class Stock:
    def __init__(self,stockID):
        self.stockName=""
        self.stockID=stockID
        print("#"*80)
        self.dayStrList=[]          ##day���ڣ�string
        self.dateList=[]             ##date���ڣ�date��ʽ
        self.dayPriceOpenFList=[]    ##day���̼�
        self.dayPriceClosedFList=[]     ##day���̼�
        self.dayPriceHighestFList=[]    ##day��߼�
        self.dayPriceLowestFList=[]     ##day��ͼ�
        self.dayTradeVolumeFList=[]     ##day�ɽ���
        self.dayTurnOverFList=[]        ##day�ɽ���  ע���е�����û�гɽ���� �ɽ��������͹ɳ�Ȩ������
        self.dayRiseRateFList=[]        ##day�۸��Ƿ�
        self.dayWaveRateFList=[]        ##day�����Ƿ�
        self.dayOpenRateFList=[]	       ##day���̷��ȣ���Ҫ�����߿����Ϳ���
        self.dayOpenCloseRateFList=[]	##day���̼ۺͿ��̼۵Ĳ������ȣ���Ҫ�����߿����ߣ��Ϳ����ߵ�����
        self.dayRadioLinkOfTradeVolumeFList=[]  ##day�ɽ�������
        self.dayRiseOfTurnOverFList=[]  ##day�ɽ����
        self.dayPriceAverageFList=[]     ##�վ���
        self.day3PriceAverageFList=[]     ##3�վ���
        self.day5PriceAverageFList=[]     ##5�վ���
        self.day10PriceAverageFList=[]     ##10�վ���
        self.monthStrList=[]          ##�£�string
        self.monthPriceOpenFList=[]    ##month���̼�
        self.monthPriceClosedFList=[]     ##month���̼�
        self.monthPriceHighestFList=[]    ##month��߼�
        self.monthPriceLowestFList=[]     ##month��ͼ�
        self.monthTradeVolumeFList=[]     ##month�ɽ���
        self.monthTurnOverFList=[]        ##month�ɽ���  ע���е�����û�гɽ���� �ɽ��������͹ɳ�Ȩ������
        self.monthRiseRateFList=[]        ##month�۸��Ƿ�
        self.monthWaveRateFList=[]        ##month�����Ƿ�
        self.monthOpenRateFList=[]		##month���̷��ȣ���Ҫ�����߿����Ϳ���
        self.monthOpenCloseRateFList=[]	##month���̼ۺͿ��̼۵Ĳ������ȣ���Ҫ�����߿����ߣ��Ϳ����ߵ�����
        self.monthRiseOfTradeVolumeFList=[]  ##month�ɽ����Ƿ�
        self.monthRiseOfTurnOverFList=[]  ##month�ɽ����Ƿ�
        
        stockDataFile=os.path.join(dirData,stockID+'.txt')
        if os.path.exists(stockDataFile):
            fileOpened=open(stockDataFile,'r')
            ##���ļ��ж�ȡ�����ݣ������㹹����ص�������
            lineIndex=0
            for line in fileOpened.readlines():
                lineIndex=lineIndex+1
                splitLine=line.split()
                if lineIndex==1:
                    self.stockName=splitLine[0]
                    print(line)
                if line!="" and lineIndex>=3 and len(splitLine)>=5:
                    self.dayStrList.append(splitLine[0])
                    self.dateList.append(Ccomfunc.convertDateStr2Date(splitLine[0]))
                    
                    self.dayPriceOpenFList.append(float(splitLine[1]))
                    self.dayPriceHighestFList.append(float(splitLine[2]))
                    self.dayPriceLowestFList.append(float(splitLine[3]))
                    self.dayPriceClosedFList.append(float(splitLine[4]))
                    tradeVolume=float(splitLine[5])
                    self.dayTradeVolumeFList.append(tradeVolume)
                    turnOver=float(splitLine[6])
                    self.dayTurnOverFList.append(turnOver)
                    
                    ##�������
                    if(tradeVolume>0):
                        self.dayPriceAverageFList.append(round(turnOver/tradeVolume,2))
                    else:
                        self.dayPriceAverageFList.append(-999)

                    
                    ##�����Ƿ������
                    if len(self.dayPriceClosedFList)>=2 and self.dayPriceClosedFList[-2]>0:
						##(��������-��������)/��һ������
                        self.dayRiseRateFList.append(round(100*(self.dayPriceClosedFList[-1]-self.dayPriceClosedFList[-2])/self.dayPriceClosedFList[-2],2))
						##(�������-�������)/��һ������
                        self.dayWaveRateFList.append(round(100*(self.dayPriceHighestFList[-1]-self.dayPriceLowestFList[-1])/self.dayPriceClosedFList[-2],2))
						##(���տ���-��������)/��һ������
                        self.dayOpenRateFList.append(round(100*(self.dayPriceOpenFList[-1]-self.dayPriceClosedFList[-2])/self.dayPriceClosedFList[-2],2))
						##(��������-���տ���)/��һ������
                        self.dayOpenCloseRateFList.append(round(100*(self.dayPriceClosedFList[-1]-self.dayPriceOpenFList[-1])/self.dayPriceClosedFList[-2],2))
                    else:
                        self.dayRiseRateFList.append(-999)
                        self.dayWaveRateFList.append(-999)
                        self.dayOpenRateFList.append(-999)
                        self.dayOpenCloseRateFList.append(-999)
                    ##����ɽ����Ƿ�
                    if len(self.dayTradeVolumeFList)>=2 and self.dayTradeVolumeFList[-2]>0:
                        self.dayRadioLinkOfTradeVolumeFList.append(round(self.dayTradeVolumeFList[-1]/self.dayTradeVolumeFList[-2],2))
                    else:
                        self.dayRadioLinkOfTradeVolumeFList.append(-999)
                        
                    if len(self.dayTurnOverFList)>=2 and self.dayTurnOverFList[-2]>100:
                        self.dayRiseOfTurnOverFList.append(round(100*(self.dayTurnOverFList[-1]-self.dayTurnOverFList[-2])/self.dayTurnOverFList[-2],2))
                    else:
                        self.dayRiseOfTurnOverFList.append(-999)
            fileOpened.close()
            
            ##�������ݹ����¶ȷ�������
            ##Ϊ�˵õ��¶�����ͳ�ƽ������dateList��Ƭ��ָ�������´洢��Ԫ����
            indexYearMonthList=[]  ##����һ��List �洢 ���¶ȷ����ָ������Ԫ�飨�꣬�£���dateList��ʼ�±꣬��dateList�����±꣩
            indexStart=0
            for i in range(1,len(self.dateList)):
                itemCur = self.dateList[i]
                itemBefore=self.dateList[i-1]
                if  itemCur.month!=itemBefore.month or itemCur.year!=itemBefore.year:
                    dictIndex={}
                    dictIndex["year"]=itemBefore.year
                    dictIndex["month"]=itemBefore.month
                    dictIndex["indexStart"]=indexStart
                    dictIndex["indexEnd"]=i-1
                    indexYearMonthList.append(dictIndex)
                    indexStart=i
                if i==len(self.dateList)-1:
                    dictIndex={}
                    dictIndex["year"]=itemCur.year
                    dictIndex["month"]=itemCur.month
                    dictIndex["indexStart"]=indexStart
                    dictIndex["indexEnd"]=i
                    indexYearMonthList.append(dictIndex)

            for item in indexYearMonthList:
#                print item  ##print dictIndex debug used
                self.monthStrList.append("{}{:02}".format(item["year"],item["month"]))
                self.monthPriceOpenFList.append(self.dayPriceOpenFList[item["indexStart"]])
                self.monthPriceClosedFList.append(self.dayPriceClosedFList[item["indexEnd"]])
                if item["indexEnd"]>item["indexStart"]: ##����һ����ֻ��1�������գ�����indexStart==indexEnd==0
                    self.monthPriceHighestFList.append(max(self.dayPriceHighestFList[item["indexStart"]:item["indexEnd"]]))
                    self.monthPriceLowestFList.append(min(self.dayPriceLowestFList[item["indexStart"]:item["indexEnd"]]))
                    self.monthTradeVolumeFList.append(sum(self.dayTradeVolumeFList[item["indexStart"]:item["indexEnd"]]))
                    self.monthTurnOverFList.append(sum(self.dayTurnOverFList[item["indexStart"]:item["indexEnd"]]))
                else:
                    self.monthPriceHighestFList.append(self.dayPriceHighestFList[item["indexEnd"]])
                    self.monthPriceLowestFList.append(self.dayPriceLowestFList[item["indexEnd"]])
                    self.monthTradeVolumeFList.append(self.dayTradeVolumeFList[item["indexEnd"]])
                    self.monthTurnOverFList.append(self.dayTurnOverFList[item["indexEnd"]])

                ##�����¶��Ƿ������
                if len(self.monthPriceClosedFList)>=2 and self.monthPriceClosedFList[-1]>0:
                    ##(��������-��������)/��һ������
                    self.monthRiseRateFList.append(round(100*(self.monthPriceClosedFList[-1]-self.monthPriceClosedFList[-2])/self.monthPriceClosedFList[-2],2))
                    ##(�������-�������)/��һ������
                    self.monthWaveRateFList.append(round(100*(self.monthPriceHighestFList[-1]-self.monthPriceLowestFList[-1])/self.monthPriceClosedFList[-2],2))
                    ##(���տ���-��������)/��һ������
                    self.monthOpenRateFList.append(round(100*(self.monthPriceOpenFList[-1]-self.monthPriceClosedFList[-2])/self.monthPriceClosedFList[-2],2))
                    ##(��������-���տ���)/��һ������
                    self.monthOpenCloseRateFList.append(round(100*(self.monthPriceClosedFList[-1]-self.monthPriceOpenFList[-1])/self.monthPriceClosedFList[-2],2))
                else:
                    self.monthRiseRateFList.append(-999)
                    self.monthWaveRateFList.append(-999)
                    self.monthOpenRateFList.append(-999)
                    self.monthOpenCloseRateFList.append(-999)
            if len(self.dayStrList)>0:
                print("���ݶ�ȡ���,���ݿ�ʼ�գ�\t"+self.dayStrList[0]+"\t���ݽ����գ�\t"+self.dayStrList[-1]+ \
                       "\t���̼ۣ�\t"+str(self.dayPriceClosedFList[-1]))
            else:
                print("������Ϊ��")

        else:
            print(stockID+"���ݲ�����")

if __name__=="__main__":
    print("\n"+"#"*80)
    print ("�����з��գ�����������Ļ��ᣬ������Ҫ���ģ�����̬��Ҫ���档")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##��¼����ʼ����ʱ��
    shStock=Stock('999999')
    
    curStock=Stock('600178')
    print shStock.dayPriceOpenFList[-10:],shStock.stockID,shStock.stockName
    print curStock.dayPriceOpenFList[-10:],curStock.stockID,curStock.stockName
    print curStock.dayPriceAverageFList[-10:]
    
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))


