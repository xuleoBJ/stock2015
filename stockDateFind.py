import os
import shutil
import time
import datetime
import math
import Cstock


##���㰴���ڼ�����ͣ����

lineWrited=[]

def convertDateStr2Date(dateStr):
    split1=dateStr.split('/')
    return datetime.date(int(split1[0]),int(split1[1]),int(split1[2]))

if __name__=="__main__":
    print("\n"+"#"*80)
    print ("���Ʒ��գ��������ģ�̬�����档")
    print ("�����������鲻ȷ��ʱ�������β��15����������")
    print ("����ʷK����Ѱ��������������Ϣ�����ڣ���Ϊ��ʷ���ظ��ģ�����Ҳ��ѭ���ġ�")
    print("\n"+"#"*80)
    
    startClock=time.clock() ##��¼����ʼ����ʱ��
   
    ##��ȡ��ָ֤������
    ##shStock=Cstock.StockSH()
    

    ##��ȡ��Ʊ���룬�洢��curStock��
    stockID="002573"
    curStock=Cstock.Stock(stockID)
    
    ##����ļ���
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    fileWrited.write(stockID+'\n')

    ##���÷�������
    iDaysPeriodUser=len(curStock.dateStrList)
    ##��ʼ�������� dateStrStart
    dateStrStart=curStock.dateStrList[-iDaysPeriodUser]
    ##���˷������� dateStrEnd
    dateStrEnd=curStock.dateStrList[-1]

    print ("���ڲ�����ʷK�����ڣ�������������ѡ�꣬��ע�⿴K�����ƣ�ͬʱע��ɽ����ı��֣�")
    ##��Ҫ�������ѡ��

    ## �Ƿ��ǳɽ������ӻ��߼��٣�1���� 0 ������
    isConsiderVOlume=0 
    
    kDays=3 ##��Ҫ������K������
    for i in range(kDays):
	    print(curStock.dateStrList[-kDays+i],",rate",curStock.riseRateFList[-kDays+i],"turnOver",curStock.riseOfTurnOverFList[-kDays+i])
    bias=0.5 ##�Ƿ�ȡֵ��Χ��������1������ָ����0.5
    if stockID!="999999":
        bias=1.0 
    for i in range(-iDaysPeriodUser+kDays,-1):
	    iCount=0
	    bSelect=True
	    while iCount<=kDays-1 and bSelect==True:
		    valueRate=math.floor(curStock.riseRateFList[-iCount-1]/bias)*bias
		    if not valueRate<=curStock.riseRateFList[i-iCount]<=valueRate+bias:
			    bSelect=False
		    ##�ɽ���Ҫͬ�����ӻ��߼���
		    if isConsiderVOlume==1 and curStock.riseOfTradeVolumeFList[i-iCount]>0 and \
                       not curStock.riseOfTradeVolumeFList[-iCount-1]/curStock.riseOfTradeVolumeFList[i-iCount]>=0: 
			    bSelect=False
		    iCount=iCount+1
	    if bSelect==True:
		    print(curStock.dateStrList[i],curStock.riseRateFList[i-2],curStock.riseRateFList[i-1],curStock.riseRateFList[i],\
                          "RiseRateofNextTradeDay: "+str(curStock.riseRateFList[i+1]))
    for line in lineWrited:
        fileWrited.write(line+'\n')
    fileWrited.close()
    timeSpan=time.clock()-startClock
    print("Time used(s):",round(timeSpan,2))
  ##  raw_input()


