# -*- coding: utf-8 -*-  
import os
import shutil
import time
import datetime
import sys
import Cstock
import Ccomfunc

stockID="999999"
lineWrited=[]

##�����Ƿ����ڶ������Ʒ���
##fList����Ҫ����������list�������Ƿ������߸߿����ݣ�flow���������������ֵ��fHigh���������������ֵ
def countTrendByRiseRate(curStock,fList,fLow,fHigh):
    fSelectList=[] 
    for k in range(0,len(curStock.dayRiseRateFList)-1):
        if fLow<=curStock.dayRiseRateFList[k]<=fHigh:
            fSelectList.append(fList[k+1])
    print("��������������{},>0�ĸ���{}".format(len(fSelectList),len(filter(lambda x:x>0,fSelectList))))

##���ݵ�һ������ƣ��ڶ������Ʒ���
##fList����Ҫ����������list�������Ƿ������߸߿����ݣ�flow���������������ֵ��fHigh���������������ֵ
def countTrendByOpenCloseRate(curStock,fList,fLow,fHigh):
    fSelectList=[] 
    for k in range(0,len(curStock.dayOpenCloseRateFList)-1):
        if fLow<=curStock.dayRiseRateFList[k]<=fHigh:
            fSelectList.append(fList[k+1])
    print("��������������{},>0�ĸ���{}".format(len(fSelectList),len(filter(lambda x:x>0,fSelectList))))

def trend(curStock):
    print ("��ȥ3��ͬ��20�����������ƣ�")
    today=datetime.date.today()
    for i in [1,2,3]:
        todayLastYear=today-datetime.timedelta(days=365*i) ##��׼ȷ���ǿ���
        print "{}��ͬ���Ƿ���".format(todayLastYear.year)
        for item in curStock.dateList:
            if todayLastYear-datetime.timedelta(days=1)<=item<=todayLastYear+datetime.timedelta(days=10):
                _index=curStock.dateList.index(item)
                print curStock.dayStrList[_index],curStock.dayRiseRateFList[_index]

if __name__=="__main__":
   
    Ccomfunc.printInfor()
    
    startClock=time.clock() ##��¼����ʼ����ʱ��

    ##��ȡ��Ʊ���룬�洢��curStock��
    curStock=Cstock.Stock(stockID)
    curStock.list2array()
    
    ##��ȥ����ͬ�ڵ��Ƿ����Ƿ������������������գ�ͬ����������С��
  
    ##����ļ���
    goalFilePath='result.txt'
    fileWrited=open(goalFilePath,'w')
    fileWrited.write(stockID+'\n')

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


