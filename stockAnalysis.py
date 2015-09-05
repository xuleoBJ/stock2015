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

if __name__=="__main__":
    Ccomfunc.printInfor()
    
    startClock=time.clock() ##��¼����ʼ����ʱ��

    ##��ȡ��Ʊ���룬�洢��curStock��
    stockID="002673"
    curStock=Cstock.Stock(stockID)

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

    ##������ͬ���������ڣ�ͳ�Ʋ�ͬ�Ƿ��ĸ���Ƶ��
    for days in [300,150,90,60,30,20,10,5]:
        headLine=str(days)+"����������ͳ�ƣ�\n�Ƿ��������:\t"
        print(headLine)
        fileWrited.write(headLine+"\n")
        for i in range(-10,11):
            _line=""
            _num=len(filter(lambda x:i==int(x),curStock.dayRiseRateFList[-days:]))
            if i==10:
                _line="��ͣ��\t"+str(_num)
            else :
                _line=str(i)+"��"+str(i+1)+"\t"+str(_num)
            print _line
            fileWrited.write(_line+'\n')
    
    ##������ͬ���������ڣ�ͳ�Ʋ�ͬ�������ȵĸ���Ƶ��
    for days in [300,150,90,60,30,20,10,5]:
        headLine=str(days)+"����������ͳ�ƣ�\n����������:\t"
        print(headLine)
        fileWrited.write(headLine+"\n")
        for i in range(0,21):
            _line=""
            _num=len(filter(lambda x:i==int(x),curStock.dayWaveRateFList[-days:]))
            _line=str(i)+"��"+str(i+1)+"\t"+str(_num)
            print _line
            fileWrited.write(_line+'\n')
    
    ##������ͬ���������ڣ�ͳ�����ֵ�ĸ���Ƶ��
    for days in [300,150,90,60,30,20,10,5]:
        headLine=str(days)+"����������ͳ�ƣ�\n���ֵ�������:\t"
        print(headLine)
        fileWrited.write(headLine+"\n")
        for i in range(-10,11):
            _line=""
            _num=len(filter(lambda x:i==int(x),map(lambda x,y:100*(x-y)/y,curStock.dayPriceLowestFList[-days:],curStock.dayPriceClosedFList[-days-1:-1])))
            if i==10:
                _line="��ͣ��\t"+str(_num)
            else :
                _line=str(i)+"��"+str(i+1)+"\t"+str(_num)
            print _line
            fileWrited.write(_line+'\n')

    ##������ͬ����������,�߿����ߣ��ڶ�����ǵ�
    for i in range(-10,11):
        print("��������{}%-{}%�������Ƿ��ֲ���".format(i,i+1))
        countTrendByOpenCloseRate(curStock,curStock.dayRiseRateFList,i-0.1,i+0.1)
    ##������ͣ�棬�ڶ���߿���Ƶ��


    print("����ͷ����Ƿ����Դ������ݽ��з���Ԥ�⣺")
    for i in range(-10,11):
        print("�����Ƿ�{}%-{}%,���ո߿��ֲ���".format(i,i+1))
        countTrendByRiseRate(curStock,curStock.dayOpenRateFList,i-0.1,i+0.1)
    for i in range(-10,11):
        print("�����Ƿ�{}%-{}%�������Ƿ��ֲ���".format(i,i+1))
        countTrendByRiseRate(curStock,curStock.dayRiseRateFList,i-0.1,i+0.1)
#    for i in range(-10,11):
#        headLine=str(len(fList))+"��ǰһ���Ƿ����䣺"+str(j)+"��"+str(j+1)+",���տ��̷������䣺" if i!=10 else "ǰһ����ͣ��,���տ��̷������䣺"
#        headLine=headLine+str(i)+"��"+str(i+1)+"������" if i!=10 else headLine+"��ͣ��"
#        _num=len(filter(lambda x:i<=x<i+1,fList))
#        _line=headLine+"\t"+str(_num)
#        print _line
#        fileWrited.write(_line+'\n')
    ##�����������ǵ�Ƶ�ʲ���ֱ��ͼ
    ##ͳ�Ʒ��� ���ڴ��̿��̵�λ����͵�Ĳ��,���ֻ�ܽ�����Ч��������Ч
    ##���10�������յĸ����Ƕ���t��õĲο����ϡ�������ƾ�о�˵ ���ˣ����߸��ˣ�������
    ##�����������ǵ�Ƶ�ʲ���ֱ��ͼ
    ##�����������ǵ�Ƶ�ʲ���ֱ��ͼ
    ##�����߿����ߣ��Ϳ����ߣ��߿����ߣ��Ϳ����ߵĸ���
    ##����ÿ������ķ��ȷֲ�����ͼ
    ##��ͣ���ߵ�ͣ���ֵĸ���
    ##�߿����������Ϳ�������
    ##���÷�������
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
  ##  raw_input()


